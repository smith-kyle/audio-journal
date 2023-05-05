## :studio_microphone: Notion Audio Journal

For those who love Notion, want to use it as a journal, but don't want to touch a computer at night.

### How it works

For now, this is a CLI app, so there is _some_ computer touching involved.

1. Hit space to record
2. Say your peace
3. Space again to stop

Your audio will be trascribed on-device and uploaded directly to Notion.

### Getting started

- Create a [Notion integration](https://www.notion.so/my-integrations)
- Create a page in Notion that you wish to use as a journal.
- Grant the integration access to the journal page by visiting the page in your Notion workspace, clicking the ••• menu at the top right of a page, **scrolling down** to Add connections
- Find the page ID by clicking Share > and noting the last 32 character string
- Update the `.env` with your page ID and integration key

```
pip install -r requirements.txt
sudo python main.py
```
