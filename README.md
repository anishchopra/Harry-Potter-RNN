# Harry-Potter-RNN
A recurrent neural network that was trained using the entire text of "Harry Potter and the Goblet of Fire" to generate new Harry Potter text.

I attempted to train this using a statefull RNN that takes in one character at a time and produces one character at a time. I also attempted to train a stateless RNN that takes in a window of 100 characters and produces one character at a time. The latter turned out to be much more effective. I have included both models so you can see for yourself.

Here is some output from the stateless recurrent neural network that takes predicts characters one at a time, using a seed text of 100 characters (with some autocorrect applied):

SEED TEXT:
 behind them.  at the same moment, bill, charlie, and percy emerged from the boys' tent, fully dress


PREDICTED TEXT:
ed as though he was standing at him i was standing at the goblet of forest to the triwizard tourn



SEED TEXT:
le divination this afternoon," harry groaned, looking down.  divination was his least favorite subje


PREDICTED TEXT:
CTT he was standing at the compartment and stared at him i was standing at the dark lord and he w



SEED TEXT:
t because we know the dementors are standing guard at azkaban!"
"the rest of us sleep less soundly i


PREDICTED TEXT:
n the triwizard tournament i was standing at the goblet of forest to the triwizard tournament to



SEED TEXT:
ccupied the carriages in front were already hurrying up the stone steps into the castle. harry, ron,


PREDICTED TEXT:
and Hermione was standing at the compartment and stared at him i was standing at the goblet of fo



SEED TEXT:
've got more points on the second task," said cedric mulishly.  "you stayed behind to get all the ho


PREDICTED TEXT:
use of the triwizard tournament i was standing at the stands on the grounds he was standing at t

### If attempting to train this on your own computer, I highly reccommend that you use a GPU, as recurrent neural networks take a long time to train. 
