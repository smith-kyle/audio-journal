# :studio_microphone: Notion Audio Journal

> Want to journal more? Hate writing by hand?

## How it works

1. Hit space to record
2. Say your peace
3. Hit space again to stop

Your audio will be trascribed on-device and uploaded directly to Notion.

https://user-images.githubusercontent.com/5474861/236587909-a7b0578b-b742-4571-80a2-65e249c43fca.mp4

## Why?

I wish I journaled more often. The ability to look back through the years, reflect and remember events long past is invaluable.

While the benefits of hand written journaling are clear, forcing one to slow down, to organize one's thoughts, I find the 5x slow down makes it a non-starter. So instead lets optimize for gross word count!

## Getting started

- Create a [Notion integration](https://www.notion.so/my-integrations)
- Create a page in Notion
- Grant the integration access to the page ([docs](https://developers.notion.com/docs/authorization#integration-permissions))
- Update the `.env` with your [page ID](https://github.com/ramnes/notion-sdk-py/discussions/31) and integration key

```
pip install -r requirements.txt
sudo ./run.sh
```

## Future work

- Deploy to a raspberry pi
- Interface with a push to talk microphone
- Integrate with other document storage options e.g. Google docs
