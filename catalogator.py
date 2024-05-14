from cat.mad_hatter.decorators import hook
from typing import Dict


def parse_metadata(metadata_str: str) -> Dict[str, str]:
    metadata={}
    for item in metadata_str.split(';'):
        key,value = item.split(':', 1)
        metadata[key.strip()] = value.strip()
    return metadata

@hook
def before_rabbithole_stores_documents(docs, cat):

    # Load settings
    settings = cat.mad_hatter.plugins["catalogator"].load_settings()
    raw_metadata = settings["document_metadata"]

    metadata_obj = {}

    if raw_metadata:
        metadata_obj = parse_metadata(raw_metadata)
        for d, doc in enumerate(docs):
            if metadata_obj is not None:
                doc.metadata.update(metadata_obj)

    return docs

@hook 
def before_cat_recalls_declarative_memories(declarative_recall_config, cat):
    if cat.working_memory['user_message_json']['filter_declarative_memory']:
        declarative_recall_config["metadata"] = cat.working_memory['user_message_json']['filter_declarative_memory']

    return declarative_recall_config