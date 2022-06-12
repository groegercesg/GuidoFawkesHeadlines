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

With this completed, we are about to use the model to predict the end on sentences based on starts. We comb through the data to find the most common first word, first two words and first three words. We then pop these into the model, to generate some sample headlines. To get a prediction from the model, you have

## Results

----------------
Using the array: most_popular_first_word
Labour:
	With length of 14:
		Labour Party A Day Makes Evil The World
		Labour Law Review Review in London , Smith &
		Labour from The Living Plan ? The Democracy Campaign
	With length of 21:
		Labour Government Strike Cost Scrutiny Project under the National Health Service Commission ,
		Labour Parliament Coup by Labour Party senior lawyers , Labour and Labour him , David
		Labour Labour Party Campaign Party Investigation Committee Vice - President Keith Eric
WATCH:
	With length of 14:
		WATCH : The Last Stand on Sky Sunday , off -
		WATCH : The Lost Mystery of Tim Hunt and The
		WATCH : The Last Words : a Blog About Love
	With length of 21:
		WATCH : The Past Days : The Story of Talk That Talk , a
		WATCH : The Guy Wants To Last Day Christmas Live ! turn Party against
		WATCH : The War Years on BBC Wales : The Daily BBC News from
Corbyn:
	With length of 14:
		Corbyn Google Face Off Chat Show Google .
		Corbyn Live in Britain Live ? , Live at Oxford
		Corbyn No . 3 Holy Ground Church , Puts
	With length of 21:
		Corbyn of the israeli Snap Army conference of 12 March 2013 : The Left Wing of
		Corbyn They Do i Do Love As a Feminist . They write , work of
		Corbyn seven months after work Canada is exposed to an attacking force , during which the Red Army removed
BBC:
	With length of 14:
		BBC Three Hitler : The History of Britain website (
		BBC The Video Footage 2 by Bennett : Best
		BBC The Night Breaking : The Time Machine
	With length of 21:
		BBC Only Things ( Good Things New ) Week , March 3 , 2014 .
		BBC Sex in the Sunday : BBC One and All you Need for Living
		BBC Russell Michael Hall : Travel Stories That Happened Before It Is
The:
	With length of 14:
		The Take Off Again : From Set to Kill
		The Doctor Who Stories take - back and position , a
		The Graham Goodbye : For Journalists and Wrong End
	With length of 21:
		The British Set Off On and When You Were Tomorrow ! , London
		The Teenage Hated Girls in George ; Greatest Hits Only Been Produced
		The Hot Prime Star ( Greatest Hits ) which was first broadcast in South China
Tory:
	With length of 14:
		Tory Lee House Cabinet Cabinet Cabinet Cabinet of
		Tory Oxford English Picture Film of the Week as
		Tory Parliament Black Cabinet Cabinet Cabinet Office Cabinet
	With length of 21:
		Tory MP Private Party Cambridge won the presidential election for the Sex and City Council
		Tory Prime Minister John Williams confirmed this issue , following his re - election in March 2015
		Tory Parliament parliament mps and mps are Commons constituency list into standing seats on parliamentary seats . On
EU:
	With length of 14:
		EU members of Parliament ( MP ) for Parliament James or
		EU Parliament Debate Parliament ( Northern Ireland ) published on
		EU Parliament Debate , 2015 : Lord Justice Party
	With length of 21:
		EU That Does It Again ? UK EU Council Member 2014
		EU Parliament Heads Meeting Lord President of Canada ; Foreign and Foreign Minister
		EU World Office Special Edition , London , Scotland : The Guardian
PMQs:
	With length of 14:
		pmqs ( The New Order Single Camera double card media
		pmqs BBC Three Day Last ! : British Prime
		pmqs Record of Double Donation ! : Big Boss
	With length of 21:
		pmqs BBC Two pictures of Oxford Parliament House of Commons Down , men in
		pmqs A Man Goes to the Land of Black Sun Killing My Life
		pmqs the Russian Civil War and Hitler Front Crash Project of Iran and
Owen:
	With length of 14:
		Owen George PM here in North America first Tony
		Owen Jones , Keith Anderson , Peter Murphy , and
		Owen Northern Pass Hospital Hospital are Christian Blue
	With length of 21:
		Owen Owen Owen ( Owen Owen ) in the British Royal Army from the time
		Owen Brown Mitchell ( who went on to serve as chief of the staff of World War i
		Owen Hunt on set from The Churchill Falls Final Report ( Mike Coventry and
Diane:
	With length of 14:
		Diane Jones : Best of Will Anna , Co -
		Diane Churchill , Secretary of State for Foreign Policy and
		Diane Lucas : Best of Diane Lucas Christmas Special
	With length of 21:
		Diane Watson ( has a Nazi name ) and Constance Watson ( a British daughter ) are
		Diane Lewis : Is There Comes Another Man ? ( Made To Tell
		Diane Strike in London and Oxford Street Attack of Change by Clash for Family

----------------
Using the array: most_popular_two_words
PMQs SKETCH:
	With length of 14:
		pmqs SKETCH : The Next Party Crash : Fake Story
		pmqs SKETCH : The Next Morning Line by Andy Miller and
		pmqs SKETCH : The Sketch Project takes a line from the National
	With length of 21:
		pmqs SKETCH : The Private Eye Show , SKETCH shows on The Office , America :
		pmqs SKETCH : The Next Act SKETCH ( SKETCH ) , SKETCH , SKETCH , or
		pmqs SKETCH : The Return of the Show ( Channel 4 story ) and Reality TV :
Owen Jones:
	With length of 14:
		Owen Jones and Motion Picture Star Motion Picture Show :
		Owen Jones Hall Presidential Election for President Majority ( 2014 )
		Owen Jones or Harry Harry Jones as Be Elected Secretary
	With length of 21:
		Owen Jones ( The Christian Activist Had Rally ) , a British political and political activist had
		Owen Jones ( Adam Jones ) , who was President from March 13 , March 20 ,
		Owen Jones Jones ( Williams ) : the murphy of Jones , a Staff Officer from the
Diane Abbott:
	With length of 14:
		Diane Abbott Meets House Nurse Week , May 4 , 2013
		Diane Abbott ( Twitter channel as Charles Made ) on The
		Diane Abbott ( 2013 ) , for the Family Guy : The
	With length of 21:
		Diane Abbott reveals a lesbian and gay female high school student who was from a London hospital was arrested , and she
		Diane Abbott Stories Are My Girls Next Issue Edition of the New Deal
		Diane Abbott on The Same Old Column before her death in The Won Or Never
Read in:
	With length of 14:
		Read in the empty hour at an Air Service reading room officer makes one
		Read in the Bill for Office of the Director of Government
		Read in the TV and law - school as a private boy in it ,
	With length of 21:
		Read in the Oxford English English National English Sense Reading Column by the Oxford
		Read in the Act of Parliament of the British Government on Oliver Queen Queen Charlotte
		Read in the House of Lords anything things would be wrong is confirmed . a Church judge did not vote
Tory MP:
	With length of 14:
		Tory MP James Osborne Graham who seen Graham Graham was a
		Tory MP Hilary Bennett called the Voted Evidence Westminster Manifesto
		Tory MP Anne Russell Bennett during an early BBC attack on
	With length of 21:
		Tory MP Oliver Biden was an Opposition Member in the Cabinet for Foreign Policy at the
		Tory MP Martin Campbell White in having won the Seat of Parliament Voting for Parliament in
		Tory MP Red House Party Leader in Labour parliament Bill Keith Green attacked MP
Piers Morgan:
	With length of 14:
		Piers Morgan Morgan & Company Hall , Oxford , England ,
		Piers Morgan and Blue Line Road ( Friday , Oxford
		Piers Morgan and Company ( Law & Order & Appeal )
	With length of 21:
		Piers Morgan ( British Channel Channel ) are them set , for a Channel 4 broadcast in March
		Piers Morgan and Jolly Green , Class of Richard Gordon Row ( full - mouth ) (
		Piers Morgan House Can Do Only For Her Wrong Part i at the South
Labour MP:
	With length of 14:
		Labour MP Spoke What ? Over ? , published in The
		Labour MP Neil Osborne , Labour politician and Minister for Politics
		Labour MP Alan Burns , MP for Labour Party Scotland
	With length of 21:
		Labour MP Adam Graham won the Labour Politician , New South Wales Party Leader
		Labour MP For What Make Man Did For a Time on Children Spoke
		Labour MP Neil Graham , Chairman of the Labour Leadership Committee , Minister for Human
Claudia Webbe:
	With length of 14:
		Claudia Webbe from the British Channel Office : Action on Tony
		Claudia Webbe Brown Naming # 5 Personal Car Issue with
		Claudia Webbe ( The Special Doubles ) 2 : The Naked
	With length of 21:
		Claudia Webbe Smith Wind Again Wing MP - Co Writer for Sky Star
		Claudia Webbe Baker , Simon Brand and Nick Baker Jones ( Standards Officer for the
		Claudia Webbe ( Wrong She ) for Police Car Three : The Lucy Martin
Labour MPs:
	With length of 14:
		Labour mps James Joyce and Lewis Cameron Clarke called him
		Labour mps RUSSIAN calls for a Labour Party party investigation team ; it
		Labour mps Office Labour candidates Labour and Labour Party mps
	With length of 21:
		Labour mps Labour Party , Labour Party and Labour Party June Council ( Scottish
		Labour mps says they need to report about them as a candidate to vote , as a Bill Clinton has said
		Labour mps in parliament how they get voted in Parliament they say , a Scottish Parliament proposal would have been
Extinction Rebellion:
	With length of 14:
		Extinction Rebellion of 2014 a British Army campaign against Britain in Europe
		Extinction Rebellion : The War of the 70 Lives After
		Extinction Rebellion of the Father James Williamson AM Star Motion
	With length of 21:
		Extinction Rebellion of Finally We Need Johnson on Day 30 Live , Butler
		Extinction Rebellion : The Last Rebellion of Rebels by John Hancock , John MP ,
		Extinction Rebellion Group privately published in 2013 Threatened Life , New Media , and Civil Action

----------------
Using the array: most_popular_three_words
Read in Full:
	With length of 14:
		Read in Full : Nick Must Tell 10 a Day Is Gone
		Read in Full : The Schools Dead School Press Team on
		Read in Full : Live for All But Us ? ? The
	With length of 21:
		Read in Full : On the Analysis of Sex Pictures for Idea Evidence Canada : Why
		Read in Full : People Wants to Want To Change Today by Boris Falls , James
		Read in Full : The rory on the Mirror Mirror Still Flag Video by Jack Miller goes
+++ RESHUFFLE LIVE:
	With length of 14:
		+++ RESHUFFLE LIVE / TV show - off Tony Blair : a Special
		+++ RESHUFFLE LIVE Shows : Breaking Ben and Cameron Burnham Live
		+++ RESHUFFLE LIVE : Lockdown : Live Under Rule ? and past interview
	With length of 21:
		+++ RESHUFFLE LIVE ! Live ! VIEWS Friday show and Live 3 : Absolute Love ! on
		+++ RESHUFFLE LIVE again by Cameron Cooper and Co - Co George Kennedy & Paul
		+++ RESHUFFLE LIVE ? ( film is set in BBC More ) what is turned out to be the last UK
Channel 4 News:
	With length of 14:
		Channel 4 News Channel TV on Channel 4 News Channel Sunday
		Channel 4 News Scandal : The Head Girls Put Me
		Channel 4 News Channel Channel MP N Blair Labour Channel
	With length of 21:
		Channel 4 News Channel Special Coverage Show for Live During Sunday , June 2014 .
		Channel 4 News Channel Channel 4 NEWS Channel 2 Channel 8 TV Channel 12 Channel 6
		Channel 4 News Channel Channel 4 Channel 4 Channel 8 Live 2 Off Channel 4 ,
READ IN FULL:
	With length of 14:
		READ IN FULL : * * * You Win It All My
		READ IN FULL : AN Online Guide to Independent First Read
		READ IN FULL : THE Family Guy and The Job , Jim
	With length of 21:
		READ IN FULL : The End Days of The Daily Telegraph late in life . It is a
		READ IN FULL : The Mansion Life of Tom Anderson , ON : Last Thing to
		READ IN FULL : Dawn of the War Girl in the food of the snow and the dead two days after they
EXCLUSIVE: Home Office:
	With length of 14:
		EXCLUSIVE : Home Office Home Release Interview online on First Day Live
		EXCLUSIVE : Home Office Edition Edition RELEASE no . 3 : Home Office
		EXCLUSIVE : Home Office Edition Slip Box Box at the Office Box
	With length of 21:
		EXCLUSIVE : Home Office Video that was was to be the majority boss single with Home Box ! Home ! not
		EXCLUSIVE : Home Office Edition video video were first published in March 2013 . The new video even used the We
		EXCLUSIVE : Home Office : Home Behind - the - Shot Home Video Response Release It
Good Law Project:
	With length of 14:
		Good Law Project Israel Scandal Agreement Team Out Channel UK
		Good Law Project We Want This Money Now ? ( Star
		Good Law Project America , i Am Gay This Week i say
	With length of 21:
		Good Law Project ISRAEL Tax Market : Black and White Paper Against Land Tax
		Good Law Project : Bashir water member but used as a video account to support the UK . It was part
		Good Law Project : High School Years After Death Turn : Act Family Law
Labour Parliamentary Candidate:
	With length of 14:
		Labour Parliamentary Candidate : Government Draft Speech to Vote on the Party
		Labour Parliamentary Candidate : Signatures Without Cash Support Party support 10 Years
		Labour Parliamentary Candidate : Paul King , MP for Labour Wales ,
	With length of 21:
		Labour Parliamentary Candidate : Political Referendum on Parliament for Britain , UK & Ireland , Kennedy Blue
		Labour Parliamentary Candidate : Election in Britain of Free Labour ( Labour ) Leader The General
		Labour Parliamentary Candidate : Labour and Political Criticism ( BBC London ) , Labour and Labour Supporters
Lib Dem Candidate:
	With length of 14:
		Lib Dem Candidate For Disabled Man ( Face to Face ) of
		Lib Dem Candidate In Life of Maria Theresa Un Dirty
		Lib Dem Candidate , Women in Prime Office Office Scandal ,
	With length of 21:
		Lib Dem Candidate for Social Political Party ( German ) Election Reform 2014 , Commons (
		Lib Dem Candidate for Social Security Scandal of Red House Club 2 ( 2 May 2013 )
		Lib Dem Candidate For Sex ? ( Emma Britons ) Online , Op . seven a -
Emma Dent Coad:
	With length of 14:
		Emma Dent Coad Tells Water Story But Lucy Watson is
		Emma Dent Coad Whip Teen Launch Media - News Issue she
		Emma Dent Coad Show Hall House Daughter of Truth and Government
	With length of 21:
		Emma Dent Coad Parliament Question during the Show Off Parliament Committee Poll Politics Guide
		Emma Dent Coad Robinson ( 2015 – 2014 ) Her Out from Leveson Road Editor was co -
		Emma Dent Coad : The Internet Guide to the City of England , London and New
High Court Rules:
	With length of 14:
		High Court Rules against Surrey High School Schools Association of Ireland
		High Court Rules ( UK Rules ) All Year Court Order
		High Court Rules Committee Response Group ( ) report of attack on
	With length of 21:
		High Court Rules Committee Rules Committee Report Inquiry Committee TO Review Committee Standards
		High Court Rules , England for Boys Boys High School Boys , East London High
		High Court Rules of South Wales v Surrey High Court in Graham East MP Tony
