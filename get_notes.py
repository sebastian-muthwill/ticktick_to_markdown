from ticktick import api
from mdutils.mdutils import MdUtils
from mdutils.tools import Html

import config

client = api.TickTickClient(config.ticktick_user, config.ticktick_password)

uncompleted_tasks = client.state['tasks']

# list comprehension: get all tasks/notes where the tag defined in config is present
notes = (task for task in uncompleted_tasks if config.ticktick_tag in task.get('tags', []))

# create markdown file for every note
for note in notes:
    # get informations from note/task
    title = str(note.get('title'))
    content = note.get('content')
    created = note.get('createdTime')
    tags = note.get('tags')
    
    # if the note title is a link we need to get the text from it
    if title.startswith("["):
        closing = title.find("]")
        filename = title[1:closing]
        print(filename)
    else:
        filename = title

    # TODO: implement try catch and log for problems with filenames
    mdfile = MdUtils(file_name=config.md_path + filename, title=filename)

    # add header
    if config.create_note_header:
        mdfile.new_paragraph(config.note_header)

    # check if contet has link to youtube then embed
    if str(content).__contains__("://youtu.be/"):
        start = str(content).find("://youtu.be/")
        yt_link = str(content)[start+12:start+23]
        print(yt_link)
        #mdfile.new_header(level=2, title="Youtube")
        mdfile.new_paragraph(f"""<iframe width="560" height="315" src="https://www.youtube.com/embed/{yt_link}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""")

    mdfile.new_paragraph(content)
    mdfile.create_md_file()

    # TODO: delete note if setup in config
    if config.ticktick_complete_note:
        client.task.complete(note.get('id'))