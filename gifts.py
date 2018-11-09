# Copyright (c) 2018  Michael C. Tiberio  All rights reserved.

import random

def assign_gifts():
	          # Child         Parent 
	givers = [[ 'Elaina'    , 'Bernice' ],
	          [ 'Elizabeth' , 'Bernice' ],
	          [ 'Evan'      , 'Lucia'   ],
	          [ 'Jesse'     , 'Steve'   ],
	          [ 'Katherine' , 'Belinda' ],
	          [ 'Kaylee'    , 'Steve'   ],
	          [ 'Mathew'    , 'Gabe'    ],
	          [ 'Matisyn'   , 'Belinda' ],
	          [ 'Michael'   , 'Gabe'    ],
	          [ 'Natalie'   , 'Simona'  ],
	          [ 'Riley'     , 'Lucia'   ],
	          [ 'Spencer'   , 'Simona'  ]]
	receivers = givers[:]

	# Ensure givers and receivers don't have the same parent
	while (len([True for giver, receiver in zip(givers, receivers) if giver[1] == receiver[1]]) != 0):
		random.shuffle(receivers)

	# Return a list of (giver, receiver) tuples
	return zip([giver[0] for giver in givers], [receiver[0] for receiver in receivers])

if __name__ == '__main__':
	assignments = assign_gifts()
	for assignment in assignments:
		print(assignment[0] + ' gives to ' + assignment[1])
