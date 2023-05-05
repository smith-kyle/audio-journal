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
- Create a page in Notion
- Grant the integration access to the page ([docs](https://developers.notion.com/docs/authorization#integration-permissions))
- Update the `.env` with your [page ID](https://github.com/ramnes/notion-sdk-py/discussions/31) and integration key

```
pip install -r requirements.txt
sudo ./run.sh
```
