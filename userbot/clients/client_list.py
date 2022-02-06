import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, ROSE2, ROSE3, ROSE4, ROSE5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if ROSE2 is not None:
            id2 = await ROSE2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if ROSE3 is not None:
            id3 = await ROSE3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if ROSE4 is not None:
            id4 = await ROSE5.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if ROSE5 is not None:
            id5 = await ROSE5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        ROSE_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        ROSE_USER = client.first_name
    rose_mention = f"[{ROSE_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, ROSE_USER, rose_mention
