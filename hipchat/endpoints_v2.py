"""
API MAPPING FOR HipChat API V2
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/v2',

    'get_capabilities': {
        'path': '/capabilities'
    },
    'get_all_emoticons': {
        'path': '/emoticon',
        'valid_params': ['start-index', 'max-results', 'type']
    },
    'get_emoticon': {
        'path': '/emoticon/{{emoticon}}'
    },
    'get_all_rooms': {
        'path': '/room',
        'valid_params': ['start-index', 'max-results', 'include-private', 'include-archived']
    },
    'send_room_notification_redirect': {
        'method': 'POST',
        'path': '/room/{{room}}/message',
        'status': 307
    },
    'send_room_notification': {
        'method': 'POST',
        'path': '/room/{{room}}/notification',
        'status': 204
    },
    'get_room': {
        'path': '/room/{{room}}',
        'valid_params': ['expand']
    },
    'set_room_topic': {
        'method': 'PUT',
        'path': '/room/{{room}}/topic',
        'status': 204
    },
    'get_room_members': {
        'path': '/room/{{room}}/member',
        'valid_params': ['start-index', 'max-results', 'expand']
    },
    'get_room_participants': {
        'path': '/room/{{room}}/participant',
        'valid_params': ['start-index', 'max-results', 'include-offline', 'expand']
    },
    'view_history': {
        'path': '/room/{{room}}/history',
        'valid_params': ['date', 'timezone', 'start-index', 'max-results', 'reverse']
    },
    'send_private_message': {
        'method': 'POST',
        'path': '/user/{{user}}/message',
        'status': 204
    },
    'get_user':  {
        'path': '/user/{{user}}'
    },
    'get_all_users':  {
        'path': '/user',
        'valid_params': ['start-index', 'max-results', 'include-deleted', 'expand']
    },
    'update_user': {
        'path': '/user/{{user}}'
    },

}
