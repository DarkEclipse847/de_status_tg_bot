require("dotenv").config();
const {Telegraf} = require("telegraf");

const bot = new Telegraf(process.env.TOKEN);

bot.start((ctx)=>ctx.reply("Hello world"));
bot.launch();
