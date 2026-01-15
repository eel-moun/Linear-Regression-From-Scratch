🚗 ft_linear_regression

Learning Machine Learning from scratch

📌 What is this project?

This project is a simple and practical introduction to Machine Learning.

The goal is to build a small program that can predict the price of a car based on its mileage.

If we know how much a car was driven in the past and how much it was sold for, we can use this information to teach a computer to make new predictions.

That is exactly what this project does.

🧠 What does “machine learning” mean?

Machine learning means letting a computer learn from examples instead of giving it fixed rules.

Instead of saying:

“If the mileage is high, the price is low”

we give the computer many real examples:

mileage

real price

and let it discover the rule by itself.

The more examples it sees, the better it becomes.

📈 What is linear regression?

Linear regression is one of the simplest ways for a computer to learn.

It tries to find a straight line that best connects:

how much a car was driven

how much it costs

Once that line is found, the computer can use it to:

estimate the price of any new car

even if it has never seen it before

So instead of memorizing prices, the model understands the trend.

❌ How does the computer know it is wrong?

Every time the model makes a prediction, we can compare it to the real price.

If the predicted price is far from the real price, the model knows:

“I made a big mistake.”

The goal of learning is simply:

make these mistakes smaller and smaller.

🔁 How does learning happen?

The computer starts with a very bad guess.

Then it repeats this process:

Make predictions

Measure how wrong they are

Adjust itself a little

Try again

Each step makes the predictions better.

After many repetitions, the model slowly becomes accurate.

This process is called training.

🧭 Why gradient descent?

Gradient descent is just a fancy name for:

“Try to improve a little bit every time.”

The model looks at its mistakes and slightly changes how it predicts so that the next predictions are closer to the truth.

It’s like walking down a hill in the dark:

you feel the slope

you step in the direction that goes down

eventually you reach the bottom

The bottom is the best possible model.

📊 Why do we scale the data?

Mileage numbers can be very large (100,000 km, 200,000 km…).

If we give these big numbers directly to the computer, learning becomes unstable and slow.

So we first scale the data to smaller values so the model learns:

faster

more smoothly

more reliably

This is an important real-world machine learning technique.

🗂 Project structure

This project is split into two main parts:

Training program

This program:

reads the dataset

learns the relationship between mileage and price

saves what it learned

Prediction program

This program:

loads what was learned

asks for a mileage

prints the estimated price

The model is trained once, then reused many times.

🎯 Why this project is important

This project teaches the foundations of:

how machines learn

how data becomes predictions

how errors guide learning

These ideas are the same ones used in:

AI systems

self-driving cars

recommendation systems

and even ChatGPT

This is where it all starts.
