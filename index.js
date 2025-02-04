require("dotenv").config();
const {Telegraf} = require("telegraf");
const Markup = require("telegraf/markup")

const bot = new Telegraf(process.env.TOKEN);

//TODO: Need to make this unique, to find requests by id
var request_chat = 1;

//Creating button on start
bot.start((ctx)=>{
    return ctx.reply("Hi", {
        ...Markup.keyboard([
            [Markup.button.channelRequest("Выбрать канал", request_chat)]
        ]).resize()
    });
});

//This function will trigger, when user shares chat with bot
//for now it sends chat_id back to user
bot.on("chat_shared", ctx=>{
    ctx.reply(ctx.update.message.chat_shared.chat_id);
})
bot.launch();
