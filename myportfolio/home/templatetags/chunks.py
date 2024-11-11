from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    # If list_data is None or not iterable, return an empty list
    if list_data is None or not hasattr(list_data, '__iter__'):
        return []

    chunk = []
    for i, data in enumerate(list_data, start=1):
        chunk.append(data)
        if i % chunk_size == 0:
            yield chunk
            chunk = []
    
    # Yield any remaining items
    if chunk:
        yield chunk
