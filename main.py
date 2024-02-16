import numpy as np
import matplotlib.pyplot as plt
from telegram.ext import *
from dotenv import load_dotenv

import os

async def start(update, context):

    reply_string = '''
To  use the bot you need to write the command followed ny the function, than the lower and upper bound and lastly the number of points to evaluate f(x) in that interval:
e.g.
/plot sin(x)+x**2-3*x+pi 0 2 10
NO SPACES in the function description

    '''
    await update.message.reply_text(reply_string)


async def plot_tel(update, context):
    _, func, a, b, n = update.message.text.split(' ')
    a = float(a)
    b = float(b)
    n = int(n)
    x = np.linspace(a,b,n)
    eval_extra = {
    "sqrt": np.sqrt,
    "cos": np.cos,
    "sin": np.sin,
    "exp": np.sin,
    "e": np.e,
    "pi": np.pi,
    "x": x,
    "log": np.log,
    }

    y = eval(func,eval_extra)

    plt.style.use('ggplot')
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title(f"Plot of {func}")
    plt.plot(x,y)

    plt.savefig("plot.jpg")
    plt.close()
    await update.message.reply_photo("plot.jpg")




def main():

    load_dotenv()
    TELEGRAM_TOKEN = os.getenv("TOKEN")
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('plot', plot_tel))

    # Run bot
    application.run_polling()
if __name__=='__main__':
    main()

