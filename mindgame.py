
from akinator.async_aki import Akinator
import akinator
import asyncio

mind = Akinator()

async def main():
    q = await mind.start_game()

    while mind.progression <= 80:
        a = input(q + "\n\t")
        if a == "b":
            try:
                q = await mind.back()
            except akinator.CantGoBackAnyFurther:
                pass
        else:
            q = await mind.answer(a)
    await mind.win()

    correct = input(f"It's {mind.first_guess['name']} ({mind.first_guess['description']})! Was I correct?\n{mind.first_guess['absolute_picture_path']}\n\t")
    if correct.lower() == "yes" or correct.lower() == "y":
        print("Yay\n")
    else:
        print("Oof\n")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()