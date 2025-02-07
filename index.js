require("dotenv").config();
const {Telegraf} = require("telegraf");
const Markup = require("telegraf/markup");
const {spawn} = require("child_process");

const bot = new Telegraf(process.env.TOKEN);

//For now this is hardcoded, need to return something in order to check working status
function run_client(){
    const py_process = spawn("python3 client_side/bot.py")
}

//TODO: Need to make this unique, to find requests by id
var request_chat = 1;
//Creating button on start
//Fix: using start command in chat causes bot to crash
bot.start((ctx)=>{
    return ctx.reply("Hi", {
        ...Markup.keyboard([
            [Markup.button.channelRequest("Выбрать канал", request_chat)]
        ]).resize()
    });
});

//This function will trigger, when user shares chat with bot
//It sends chat id to client-side bot. this id is then processed, retrieving meme channel data cf.("client_side/bot.py")
bot.on("chat_shared", ctx=>{
    ctx.telegram.sendMessage(process.env.PRIVATE_GROUP_ID, ctx.update.message.chat_shared.chat_id)
})

bot.launch();
