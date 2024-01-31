import spacy
from dataclasses import dataclass
import spacy, re
from skweak import heuristics, gazetteers, aggregation, utils


def init():
    nlp = spacy.load('en_core_web_trf')
    NAMES = [["arddh", "aerty"]]
    trie = gazetteers.Trie(NAMES)
    detect_name = gazetteers.GazetteerAnnotator("presidents", {"NAME": trie})
    return nlp, detect_name


@dataclass()
class Entity:
    value: str
    label: str
    start: int
    end: int


if __name__ == '__main__':
    nlp, detect_names = init()
    doc = nlp("arddh")
    doc = detect_names(doc)
    entities = []
    for ent in doc.ents:
        entities.append(Entity(ent.text, ent.label_, ent.start_char, ent.end_char))
    print(entities)
