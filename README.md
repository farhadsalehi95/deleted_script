
## Authors

- [@farhadsalehi95](https://www.github.com/farhadsalehi95)


# Deleted_script

delete every file by days you want and configure notification with slack.
## Requirements

1 - apt update && apt install -y python3-pip

2 - pip install -r requirements.txt

3 - create slack workspace ==> [SLACK](https://slack.com/help/articles/206845317-Create-a-Slack-workspace)

4 - create slack webhook  ===> [SLACK_WEBHOOK](https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack)

## Running Tests

To run tests, run the following command

```bash
  python3 deleted_script.py -h
  
  python3 deleted_script.py -u YOUR_SLACK_URL -d NUMBER_OF_DAY -l LIST_OF_YOUR_DIR
```

