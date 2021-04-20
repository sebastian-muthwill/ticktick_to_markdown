from datetime import datetime

# setup your credentials and local paths as needed

# Login credentials to TickTick
ticktick_user = "<YOUR_USERNAME>"
ticktick_password = "<YOUR_PASSWORD>"

# a tag dedicated to mark notes which shall be imported as markdown
ticktick_tag = "note"

# shall the note stay in ticktick, or shall it be completed after import
# this defaults to true because otherwise files could be created again if moved from folder
# if the file exists, it will be overwriten
ticktick_complete_note = True

# note header with meta informations
# set to True if you would like to have a header in each note
# you can also drectly provide tags or backlinks here
create_note_header  = True
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
note_header = f" \
status: #seed \n \
tags: \n \
backlinks: \n \
reference: \n \
created: {timestamp} \n \
\n \
----"

# Path where to store the markdown files
# usually a folder within your obsidian vault
md_path = "/ObsidianVault/INBOX/"

