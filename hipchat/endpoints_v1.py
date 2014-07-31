"""
API MAPPING FOR HipChat API V1
"""

mapping_table = {

    'content_type': 'application/x-www-form-urlencoded',
    'path_prefix': '/v1',

    'send_message': {
        'method': 'POST',
        'path': '/rooms/message',
        'valid_params': ['format', 'auth_token']
    },

    'set_topic': {
        'method': 'POST',
        'path': '/rooms/topic',
        'valid_params': ['format', 'auth_token']
    },

}
