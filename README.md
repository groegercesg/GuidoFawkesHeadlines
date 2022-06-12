# Guido Fawkes Headlines

Using NLP Text generative models to create _fake_ Guido Fawkes headlines.

## Who?

Guido Fawkes, the _most widely read politics source in Westminster_, is a politics website that frequently breaks stories that go on to dominate newspaper pages. It's written in the character of Guido (the only man to enter parliament with honest intentions) by an editorial team who see themselves, unashamedly, as campaigning journalists. It's the bane of politicians across the political spectrum, although it must be said more so the Labour party in recent years.

## Data

In a [previous project](https://github.com/groegercesg/Guido_Fawkes_Analysis), I had previously gathered all of Guido Fawkes Saturday Seven-Up posts. These posts typically contain 7 headlines from top stories across the week. This means that I have 3353 headlines from popular Guido Fawkes stories; the popularity point is interesting, it could mean that the headlines were well liked by Guido Fawkes audience and therefore representative of the style of headlines they should be continuing to write.

## Process

With this Data, I will be performing a very minor amount of pre-processing to transform that data into a Fast AI Dataloader friendly format.

We then use a TextDataLoader to put all our headlines into one big steam, with 30% of the data used for validation.

Next we used the [AWD_LTSM](https://arxiv.org/pdf/1708.02182.pdf) model, which is well suited to generating sentences.

We train the model for 5 epochs, which took about 14 mins on my Laptop!

With this completed, we are about to use the model to predict the end on sentences based on starts. We comb through the data to find the most common first word, first two words and first three words. We then pop these into the model, to generate some sample headlines. To get a prediction from the model, you have to supply a number of words to predict. We found the average length of a headline, and ask our model to make a couple predictions. We ask it, for each starting string, to generate 3 sample headlines at double the length of the average headline and triple the length of the average headline. From preliminary testing, we found that asking it to generate headlines with just the average length was unreliable and very inconsistent.

## Results

```
Throughout these results, it should be noted that I have edited the selected outputs very lightly for clarity and concision.
Many outputs have been removed, ones that don't make much sense
Apologies to all individuals mentioned, this is the output of a statistical model that has no positions other than the input data!
```

First we'll look at the results when querying the model with the most popular first word.

**Labour:**
>   With length of 21:
>	>	Labour Government Strike Cost Scrutiny Project under the National Health Service Commission
>	>	Labour Parliament Coup by Labour Party senior lawyers

**WATCH:**
>	With length of 14:
>	>	WATCH : The Last Stand on Sky Sunday
>	>	WATCH : The Lost Mystery of Tim Hunt
>	>	WATCH : The Last Words : a Blog About Love
>	With length of 21:
>	>	WATCH : The War Years on BBC Wales

**Corbyn:**
>	With length of 21:
>	>	Corbyn at the israeli Snap Army conference of 12 March 2013
>	>	Corbyn after seven months of work Canada is exposed to an attacking force

**BBC:**
>	With length of 14:
>	>	BBC Three Hitler : The History of Britain

**Tory:**
>	With length of 14:
>	>	Tory Oxford English Picture Film of the Week
>	With length of 21:
>	>	Tory MP Private Party Cambridge won the presidential election for the Sex and City Council

**PMQs:**
>	With length of 21:
>	>	PMQs A Man Goes to the Land of Black Sun, Killing My Life
>	>	PMQs the Russian Civil War and Hitler Front Crash Project of Iran

**Owen:**
>	With length of 21:
>	>	Owen Owen Owen ( Owen Owen ) in the British Royal Army
>	>	Owen Hunt on set from The Churchill Falls Final Report

**Diane:**
>	With length of 14:
>		Diane Lucas : Best of Diane Lucas Christmas Special
>	With length of 21:
>		Diane Watson ( has a Nazi name ) and Constance Watson ( a British daughter )
>		Diane Lewis : Is There Comes Another Man ?

Next we'll look at the results when querying the model with the most popular first two words.

**Diane Abbott:**
>	With length of 14:
>	>	Diane Abbott Meets Nurse
>	With length of 21:
>	>	Diane Abbott reveals a lesbian and gay female high school student who was from a London hospital was arrested
>	>	Diane Abbott on The Same Old Column before her death in The Won Or Never

**Read in:**
>	With length of 21:
>	>	Read in the House of Lords anything wrong would be confirmed

**Tory MP:**
>	With length of 14:
>	>	Tory MP Anne Russell Bennett during a BBC attack
>	With length of 21:
>	>	Tory MP Oliver Biden was an Opposition Member in the Cabinet for Foreign Policy

**Labour MP:**
>	With length of 21:
>	>	Labour MP Neil Graham , Chairman of the Labour Leadership Committee , Minister for Humans

**Claudia Webbe:**
>	With length of 14:
>	>	Claudia Webbe Brown Naming
>	With length of 21:
>	>	Claudia Webbe MP in the Wind Again

**Labour MPs:**
>	With length of 14:
>	>	Labour mps RUSSIAN calls for a Labour Party party investigation team

**Extinction Rebellion:**
>	With length of 14:
>	>	Extinction Rebellion of 2014: a British Army campaign in Europe
>	>	Extinction Rebellion : The War of the 70 Lives
>	With length of 21:
>	>	Extinction Rebellion : The Last Rebellion of Rebels by John Hancock MP

Next we'll look at the results when querying the model with the most popular first three words.

**Read in Full:**
>	With length of 14:
>	>	Read in Full : The Schools Dead School Press Team
>	With length of 21:
>	>	Read in Full : On the Analysis of Sex Pictures

**Channel 4 News:**
>	With length of 14:
>	>	Channel 4 News Scandal : The Head Girls Put Me
>	>	Channel 4 News : The Blair Labour Channel
>	With length of 21:
>	>	Channel 4 News Channel Channel 4 NEWS Channel 2 Channel 8 TV Channel 12 Channel 6

**READ IN FULL:**
>	With length of 21:
>	>	READ IN FULL : The End Days of The Daily Telegraph
>	>	READ IN FULL : The Mansion Life of Tom Anderson

**Good Law Project:**
>	With length of 14:
>	>	Good Law Project Israel Scandal Agreement Team Up
>	>	Good Law Project We Want This Money Now ?
>	>	Good Law Project America , i Am Gay This Week i say
>	With length of 21:
>	>	Good Law Project ISRAEL Tax Market : Black and White

**Labour Parliamentary Candidate:**
>	With length of 21:
>	>	Labour Parliamentary Candidate : Criticism of Labour and Labour Supporters

**Lib Dem Candidate:**
>	With length of 14:
>	>	Lib Dem Candidate For Disabled Man ( Face to Face )
>	>	Lib Dem Candidate , Women in Office Scandal
>	With length of 21:
>	>	Lib Dem Candidate For Sex ? ( Emma Britons )

**Emma Dent Coad:**
>	With length of 14:
>	>	Emma Dent Coad Tells Water Story
>	>	Emma Dent Coad Whips Teen

**High Court Rules:**
>	With length of 14:
>	>	High Court Rules against Association of Ireland
