
# Reddit Kang Bot

A Bot which uses official Reddit api to get any new post of a specific subreddit and automatically posts to a specified channel
<br></br>
 <p align='center'>
  <a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-00ead3.svg?style=flat-square&logo=python&logoColor=00ead3&color=00ead3" /> </a>
  <a href="https://github.com/MiyukiKun/Anime_Gallery_Bot/" alt="Maintenance"> <img src="https://img.shields.io/badge/Maintained%3F-Yes-green.svg?style=flat-square&logo=serverless&logoColor=00ead3&color=00ead3" /> </a>
</p>
<br></br>

# Table of Content
- [Reddit Kang Bot](#reddit-kang-bot)
- [Table of Content](#table-of-content)
- [Features](#features)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
  - [Heroku](#heroku)
- [Known Issues](#known-issues)
- [Creator](#creator)

# Features

- Bot is just one time setup you can simply deploy and it will run without any more input
- Can choose any channel to post to or any subreddit to post from

# Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- `API_ID` You Can Get it from [here](https://my.telegram.org/) .

- `API_HASH` You Can Get it form [here](https://my.telegram.org/) .

- `BOT_TOKEN` Search [@BotFather](https://t.me/botfather) in telegram.

- `AGENT` your reddit bot user agent

- `SUBREDDIT` can add multiple subreddits by seperating them with '+'

- `APPROVAL_CHANNEL_ID` approval channel username(without the @) or if its private then use channel id (Goes without saying but add the bot to the cahannel and make admin)

- `MAIN_CHANNEL_ID` main channel where post will be posted after approval

# Deployment 

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MiyukiKun/Reddit-Kang)

# Known Issues

- The Buttons can pe pressed multipe times by user (for the life of me I cant figure out SQL to make the buttons work properly), still does not affect the main purpose of the bot.

- Sometimes posts may get repeated if the newest post gets deleted on reddit or the bot restarts (I dont know how to fix it).
  
# Creator

- [Miyuki](https://github.com/MiyukiKun/)


