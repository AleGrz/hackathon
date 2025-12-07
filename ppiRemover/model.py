import random
import re

from transformers import AutoTokenizer, pipeline
import os
import morfeusz2
import spacy
import faker

from ppiRemover import generators

faker = faker.Faker('pl_PL')

nlp = spacy.load("pl_core_news_sm")
morf = morfeusz2.Morfeusz()

tokenizer = AutoTokenizer.from_pretrained(os.path.join("ppiRemover", "model"))
ner_pipeline = pipeline(
    "token-classification",
    model=os.path.join("ppiRemover", "model"),
    tokenizer=tokenizer,
    device=-1,
    aggregation_strategy="simple"
)


def get_metadata(sentence):
    analysis = nlp(sentence)
    m_analysis = morf.analyse(sentence)

    metadata = []

    for sp, mo in zip(analysis, m_analysis):
        case = sp.morph.get("Case")
        if len(case):
            number = sp.morph.get("Number")
            count = "pl" if number == "Plur" else "sg"
            case = case[0].lower()
        else:
            if len(mo[2]):
                res = re.search(r":(\S*?):([^.:]*)", mo[2][2])
                if res:
                    count, case = res.groups()
                else:
                    count, case = "sg", "nom"
            else:
                count, case = "sg", "nom"
        morph_regex = rf":{count}:(\S*\.)*{case}(\.\S*)*"
        metadata.append(morph_regex)

    return metadata


def repair(text, ner):
    for e in ner:
        if e["entity_group"] != "0":
            safe_word = re.escape(e['word'])
            text = re.sub(rf"[\w@]*{safe_word}[\w@]*", e["entity_group"], text)
    return text


def get_result(text):
    res = ner_pipeline(text)
    word_metadata = get_metadata(text)
    cleaned = repair(text, res)
    return {
        "redacted": cleaned,
        "swapped": get_swapped(text, res, word_metadata),
    }


inflective = {
    "[name]": lambda: faker.first_name(),
    "[surname]": lambda: faker.last_name(),
    "[city]": lambda: faker.city(),
    "[sex]": generators.sex,
    "[religion]": generators.religion,
    "[school-name]": generators.sexual_orientation,
    "[sexual-orientation]": generators.sexual_orientation,
    "[health]": generators.sexual_orientation,
    "[relative]": generators.sexual_orientation,
    "[political-view]": generators.political_view,
    "[ethnicity]": generators.ethnicity,
}

non_inflective = {
    "[phone]": lambda: faker.phone_number(),
    "[email]": lambda: faker.email(),
    "[pesel]": lambda: faker.pesel(),
    "[document-number]": generators.sexual_orientation,
    "[company]": lambda: faker.company(),
    "[job-title]": lambda: faker.job(),
    "[bank-account]": lambda: faker.bank(),
    "[credit-card-number]": lambda: faker.credit_card_number(),
    "[username]": lambda: faker.user_name(),
    "[secret]": lambda: faker.password(),
    "[age]": lambda: random.randrange(1, 99),
    "[date-of-birth]": lambda: faker.date_of_birth(minimum_age=1, maximum_age=99),
    "[date]": lambda: faker.past_date(),
    "[address]": lambda: faker.address(),
}


def inflect(entity_group, metadata, base_word=None):
    word = base_word if base_word is not None else inflective[entity_group]()
    flexes = morf.generate(word)
    return next((f[0] for f in flexes if re.search(metadata, f[2])), word)


def align_tokens_with_entities(text, ner_results, word_metadata):
    tokens = list(nlp(text))
    aligned = [
        {
            "token": tok.text,
            "start": tok.idx,
            "end": tok.idx + len(tok.text),
            "meta": word_metadata[i],
            "entity_group": "0",
        }
        for i, tok in enumerate(tokens)
    ]

    for ent in ner_results:
        if ent.get("entity_group") == "0":
            continue
        ent_start, ent_end = ent.get("start"), ent.get("end")
        if ent_start is None or ent_end is None:
            continue
        for item in aligned:
            if ent_start < item["end"] and ent_end > item["start"]:
                item["entity_group"] = ent["entity_group"]
    return aligned


def swap_span(group, span):
    metas = [t["meta"] for t in span]

    if group in inflective:
        base = inflective[group]()
        head = base.split()[0] if base else base
        return inflect(group, metas[0], base_word=head)

    if group in non_inflective:
        return non_inflective[group]()

    return span[0]["token"]


def get_swapped(text, tokenized, word_metadata):
    aligned = align_tokens_with_entities(text, tokenized, word_metadata)
    res = ""

    i = 0
    while i < len(aligned):
        group = aligned[i]["entity_group"]
        if group == "0":
            res += aligned[i]["token"] + " "
            i += 1
            continue

        j = i + 1
        while j < len(aligned) and aligned[j]["entity_group"] == group:
            j += 1

        span = aligned[i:j]
        res += "[" + swap_span(group, span) + "] "
        i = j

    return res