#---------------------------------------------------------------------------
# Global Variables (programatically)
#---------------------------------------------------------------------------

AttackColor = "#e62222"
DefenseColor = "#2263e6"

BoostMarker = ("+Power", "270de920-f4ae-4c01-9f5f-71e03304ab6c")
DamageMarker = ("Damage", "63267618-6381-4920-98cc-def3e4b5e73e")

#---------------------------------------------------------------------------
# Events
#---------------------------------------------------------------------------

def loadMessage():
	table.board = "fieldOverlay"
#	notify("Use the F1 - F6 keys to move through the game phases, or press Tab to go to the next phase.")
#	notify("At the end of the turn, press F7 to pass control to the opponent.")
#	notify("After loading a deck, press F12 to draw 5 cards, or Ctrl+F12 for a mulligan.")
	

def checkDeck(player, groups):
#	whisper("Function is named checkDeck")
	mute()
	
	if len(player.deck) != 50:
		notify("WARNING: {}'s deck does not contain 50 cards!".format(player))

#---------------------------------------------------------------------------
# Table - This Card (cardaction)
#---------------------------------------------------------------------------
		
def dullOrReadyCard(card, x = 0, y = 0):
#	whisper("Function is named dullOrReadyCard")
	mute()
	if card.orientation & Rot90 == Rot90:
		card.orientation ^= Rot90
		notify("{} activates {}.".format(me, card))
	else:
		cardType = card.CardType
		if cardType != "Backup":
			card.orientation ^= Rot90
			notify("{} dulls {}.".format(me, card))
		else:
			askNum = askChoice("Did you mean to dull and gain CP?", ["Yes", "No"])
			if askNum != 1:
				card.orientation ^= Rot90
				notify("{} dulls {}.".format(me, card))
			else:
				dullAndGainCP(card, x, y)
	
def dullAndGainCP(card, x = 0, y = 0):
#	whisper("Function is named dullAndGainCP")
	mute()
	if card.CardType != "Backup":
		whisper("Only Backups can be dulled to gain CP.")
		playErrorSound()
		return
	cardElement = card.Element
	#if cardElement == "Light" or cardElement == "Dark":
	#	whisper("You cannot exhaust Light or Dark Backup characters for CP.")
	#	playErrorSound()
	#	return
		
	if card.orientation & Rot90 == Rot90:
		whisper("{} is already dulled.".format(card))
		playErrorSound()
	else:
		cardElement = card.Element
		askElement = None
		if card.Element == "Light" or card.Element == "Dark":
			askNum = askChoice("Which element of CP would you like?", ["Fire", "Ice", "Wind", "Earth", "Lightning", "Water"], ["#f4cccc", "#e4f6ff", "#d9ead3", "#ffe599", "#d9d2e9", "#cfe2f3"])
			if askNum == 1:
				askElement = "Fire"
			elif askNum == 2:
				askElement = "Ice"
			elif askNum == 3:
				askElement = "Wind"
			elif askNum == 4:
				askElement = "Earth"
			elif askNum == 5:
				askElement = "Lightning"
			elif askNum == 6:
				askElement = "Water"
	
		card.orientation ^= Rot90
		if cardElement == "Fire" or askElement == "Fire":
			me.counters["Fire CP"].value = me.counters["Fire CP"].value + 1
		elif cardElement == "Ice" or askElement == "Ice":
			me.counters["Ice CP"].value = me.counters["Ice CP"].value + 1
		elif cardElement == "Wind" or askElement == "Wind":
			me.counters["Wind CP"].value = me.counters["Wind CP"].value + 1
		elif cardElement == "Earth" or askElement == "Earth":
			me.counters["Earth CP"].value = me.counters["Earth CP"].value + 1
		elif cardElement == "Lightning" or askElement == "Lightning":
			me.counters["Lightning CP"].value = me.counters["Lightning CP"].value + 1
		elif cardElement == "Water" or askElement == "Water":
			me.counters["Water CP"].value = me.counters["Water CP"].value + 1
		#elif cardElement == "Light":
		#	me.counters["Light CP"].value = me.counters["Light CP"].value + 1
		#elif cardElement == "Dark":
		#	me.counters["Dark CP"].value = me.counters["Dark CP"].value + 1
		if askElement == None:
			notify("{} dulls {} and gains one {} CP.".format(me, card, cardElement))
		else:
			notify("{} dulls {} and gains one {} CP.".format(me, card, askElement))
		
def removePower(card, x = 0, y = 0):
	addPower(card, 0)
	
def addPower_X(card, x = 0, y = 0):
	mute()
	askNum = askInteger("How much power?", 1000)
	addPower(card, askNum)
	
def addPower_1000(card, x = 0, y = 0):
	addPower(card, 1000)

def addPower_2000(card, x = 0, y = 0):
	addPower(card, 2000)
	
def addPower_3000(card, x = 0, y = 0):
	addPower(card, 3000)
	
def addPower_4000(card, x = 0, y = 0):
	addPower(card, 4000)
	
def addPower_5000(card, x = 0, y = 0):
	addPower(card, 5000)
	
def addPower_6000(card, x = 0, y = 0):
	addPower(card, 6000)
	
def addPower_7000(card, x = 0, y = 0):
	addPower(card, 7000)
	
def addPower_8000(card, x = 0, y = 0):
	addPower(card, 8000)
	
def addPower_9000(card, x = 0, y = 0):
	addPower(card, 9000)
	
def addPower_10000(card, x = 0, y = 0):
	addPower(card, 10000)

def removeDamage(card, x = 0, y = 0):
	dealDamage(card, 0)
	
def dealDamage_X(card, x = 0, y = 0):
	mute()
	askNum = askInteger("How much damage?", 1000)
	dealDamage(card, askNum)
		
def dealDamage_1000(card, x = 0, y = 0):
	dealDamage(card, 1000)
	
def dealDamage_2000(card, x = 0, y = 0):
	dealDamage(card, 2000)
	
def dealDamage_3000(card, x = 0, y = 0):
	dealDamage(card, 3000)
	
def dealDamage_4000(card, x = 0, y = 0):
	dealDamage(card, 4000)
	
def dealDamage_5000(card, x = 0, y = 0):
	dealDamage(card, 5000)
	
def dealDamage_6000(card, x = 0, y = 0):
	dealDamage(card, 6000)
	
def dealDamage_7000(card, x = 0, y = 0):
	dealDamage(card, 7000)
	
def dealDamage_8000(card, x = 0, y = 0):
	dealDamage(card, 8000)
	
def dealDamage_9000(card, x = 0, y = 0):
	dealDamage(card, 9000)
	
def dealDamage_10000(card, x = 0, y = 0):
	dealDamage(card, 10000)
		
def declareAttack(card, x = 0, y = 0):
#	whisper("Function is named declareAttack")
	mute()
	if card.CardType != "Forward":
		whisper("Only Forwards can declare attacks.")
		playErrorSound()
		return
	
	card.highlight = AttackColor
	notify("{} declares an attack with {}.".format(me, card))
	
def declareDefense(card, x = 0, y = 0):
#	whisper("Function is named declareDefense")
	mute()
	if card.CardType != "Forward":
		whisper("Only Forwards can defend against attacks.")
		playErrorSound()
		return
	
	card.highlight = DefenseColor
	notify("{} defends with {}.".format(me, card))
	
def stopAttackingOrDefending(card, x = 0, y = 0):
	#	whisper("Function is named stopAttackingOrDefending")
	mute()
	card.highlight = None

#---------------------------------------------------------------------------	
# Table - Go to Phase... (groupaction)
#---------------------------------------------------------------------------

def nextPhase(group, x = 0, y = 0):
#	whisper("Function is named goToActivePhase")
	mute()
	currentPhase = getGlobalVariable("PHASE")
	if currentPhase == "Start of Game" or currentPhase == "Start of Turn": goToActivePhase(group)
	elif currentPhase == "Active Phase": goToDrawPhase(group)
	elif currentPhase == "Draw Phase": goToMainPhaseFirst(group)
	elif currentPhase == "Main Phase (1)": goToAttackPhase(group)
	elif currentPhase == "Attack Phase": goToMainPhaseSecond(group)
	elif currentPhase == "Main Phase (2)": goToEndPhase(group)
	elif currentPhase == "End Phase": passControlToOpponent(group)

def goToActivePhase(group, x = 0, y = 0):
#	whisper("Function is named goToActivePhase")
	mute()
	
	nobodyIsActive = True
	if turnNumber() == 0:
		for person in players:
			if person.isActivePlayer == True:
				nobodyIsActive = False
		
		if nobodyIsActive == True:
			askNum = askChoice("Are you playing first?", ["Yes", "No"])
			if askNum != 1:
				return
			else:
				me.setActivePlayer()
				# rnd Forces update
				rnd(1, 2)
				update()
				playSound("newTurn")
				notify("NOTE: When you play cards from your hand, they should be on 'your' side of the table (the bottom). If this isn't working properly, press F10 to (hopefully!) correct it. Otherwise, just drag the cards to your side of the field.")
	
	if me.isActivePlayer == False: return
	notify("{} enters the Active Phase.".format(me))
	
	myCharacters = (card for card in table 
						if card.controller == me
						and card.owner == me)
	wasReadied = False
	
	for card in myCharacters:
		card.orientation &= ~Rot90
		wasReadied = True
		
	if wasReadied == True:
		notify("All of their characters are activated.")
	else:
		notify("They have no characters to activate.")
	
	setGlobalVariable("PHASE", "Active Phase")
	
def goToDrawPhase(group, x = 0, y = 0):
#	whisper("Function is named goToDrawPhase")
	mute()
	if me.isActivePlayer == False: return
	notify("{} enters the Draw Phase.".format(me))
	
	if len(me.deck) == 0:
		notify("{} has no cards in their deck!".format(me))
		notify("{} loses!".format(getActivePlayer()))
		return
	
	isFirstTurn = getGlobalVariable("FIRST_TURN")
	if isFirstTurn == "True":
		drawCard(me.deck)
	else:
		drawManyCards(me.deck, x, y, 2)
		
	setGlobalVariable("PHASE", "Draw Phase")
	

def goToMainPhaseFirst(group, x = 0, y = 0):
#	whisper("Function is named goToMainPhaseFirst")
	mute()
	if me.isActivePlayer == False: return
	notify("{} enters the first Main Phase.".format(me))
	
	setGlobalVariable("PHASE", "Main Phase (1)")
	
def goToAttackPhase(group, x = 0, y = 0):
#	whisper("Function is named goToAttackPhase")
	mute()
	if me.isActivePlayer == False: return
	notify("{} enters the Attack Phase.".format(me))
	
	setGlobalVariable("PHASE", "Attack Phase")
	
def goToMainPhaseSecond(group, x = 0, y = 0):
#	whisper("Function is named goToMainPhaseSecond")
	mute()
	if me.isActivePlayer == False: return
	notify("{} enters the second Main Phase.".format(me))
	
	setGlobalVariable("PHASE", "Main Phase (2)")
	
	allCards = (card for card in table)
	for card in allCards:
		card.highlight = None
	
def goToEndPhase(group, x = 0, y = 0):
#	whisper("Function is named goToEndPhase")
	mute()
	if me.isActivePlayer == False: return
	notify("{} enters the End Phase.".format(me))
	
	setGlobalVariable("PHASE", "End Phase")
	
def passControlToOpponent(group, x = 0, y = 0):
#	whisper("Function is named passControlToOpponent")
	mute()
	if me.isActivePlayer == False: return
	
	if len(me.hand) > 5:
		whisper("You must discard from your hand until you only have 5 cards in your hand.")
		playErrorSound()
		return
	
	newTurnPlayer = getInactivePlayer()
	newTurnPlayer.setActivePlayer()
	notify("It is now {}'s turn.".format(newTurnPlayer))
	playSound("newTurn")
	setGlobalVariable("FIRST_TURN", "False")
	setGlobalVariable("PHASE", "Start of Turn")
	
	me.counters["Damage Taken"].value = len(me.piles["Damage Zone"])
	allCards = (card for card in table)
	for card in allCards:
		card.markers[DamageMarker] = 0
	
	update()

#---------------------------------------------------------------------------	
# Table - Dice and Coins (groupaction)
#---------------------------------------------------------------------------

def rollSixSidedDice(group, x = 0, y = 0):
#	whisper("Function is named rollSixSidedDice")
	mute()
	randomNum = rnd(1, 6)
	notify("{} rolls a {} from a six-sided die.".format(me, randomNum))
	
def rollManySidedDice(group, x = 0, y = 0):
#	whisper("Function is named rollManySidedDice")
	mute()
	askNum = askInteger("Roll a die with how many sides?", 20)
	if askNum < 2:
		whisper("You can't roll a die without at least two sides.")
		playErrorSound()
		return
	randomNum = rnd(1, askNum)
	notify("{} rolls a {} from a {}-sided die.".format(me, randomNum, askNum))
	
def flipCoin(group, x = 0, y = 0):
#	whisper("Function is named flipCoin")
	mute()
	randomNum = rnd(1, 2)
	if randomNum == 1:
		notify("{} flips Heads.".format(me))
	else:
		notify("{} flips Tails.".format(me))

#---------------------------------------------------------------------------
# Player - Hand - This Card (cardaction)
#---------------------------------------------------------------------------

def verifyAndPlayCard(card, x = 0, y = 0):
#	whisper("Function is named verifyAndPlayCard")
	mute()
	
	cardElement = card.Element
	fireCounterValue = me.counters["Fire CP"].value
	iceCounterValue = me.counters["Ice CP"].value
	windCounterValue = me.counters["Wind CP"].value
	earthCounterValue = me.counters["Earth CP"].value
	lightningCounterValue = me.counters["Lightning CP"].value
	waterCounterValue = me.counters["Water CP"].value
#	lightCounterValue = me.counters["Light CP"].value
#	darkCounterValue = me.counters["Dark CP"].value
	
	if (cardElement == "Fire" and fireCounterValue == 0) or (cardElement == "Ice" and iceCounterValue == 0) or (cardElement == "Wind" and windCounterValue == 0) or (cardElement == "Earth" and earthCounterValue == 0) or (cardElement == "Lightning" and lightningCounterValue == 0) or (cardElement == "Water" and waterCounterValue == 0):
		whisper("You need at least 1 {} CP in order to play {}".format(cardElement, card))
		playErrorSound()
		return
	
#	cpTotal = fireCounterValue + iceCounterValue + windCounterValue + earthCounterValue + lightningCounterValue + waterCounterValue + lightCounterValue + darkCounterValue
	cpTotal = fireCounterValue + iceCounterValue + windCounterValue + earthCounterValue + lightningCounterValue + waterCounterValue
	cardCP = int(card.CP)
	if cpTotal < cardCP:
		whisper("You have {} CP. You need at least {} CP to play {}.".format(cpTotal, cardCP, card))
		playErrorSound()
		return
		
	playMode = getGlobalVariable("PLAY_MODE")
	
	cardType = card.CardType;
	if cardType == "Summon":
		if me._id == 1:
			if playMode == "Default":
				card.moveToTable(rnd(460, 500), rnd(110, 130))
			else:
				card.moveToTable(rnd(460, 500), rnd(-262, -242))
		else:
			if playMode == "Default":
				card.moveToTable(rnd(460, 500), rnd(-262, -242))
			else:
				card.moveToTable(rnd(460, 500), rnd(110, 130))
	else:
		askNum = askChoice("Which spot do you want to play the character?", ["1 (Leftmost)", "2 (Center Left)", "3 (Center)", "4 (Center-Right)", "5 (Rightmost)"])
		cardX = -47
		if askNum == 1: cardX = -447
		elif askNum == 2: cardX = -227
		elif askNum == 4: cardX = 153
		elif askNum == 5: cardX = 353
		if cardType == "Forward":
			if me._id == 1:
				if playMode == "Default":
					card.moveToTable(cardX, 40)
				else:
					card.moveToTable(cardX, -172)
			else:
				if playMode == "Default":
					card.moveToTable(cardX, -172)
				else:
					card.moveToTable(cardX, 40)
		elif cardType == "Backup":
			if me._id == 1:
				if playMode == "Default":
					card.moveToTable(cardX, 230)
				else:
					card.moveToTable(cardX, -362)
			else:
				if playMode == "Default":
					card.moveToTable(cardX, -362)
				else:
					card.moveToTable(cardX, 230)
			card.orientation ^= Rot90
			
#	notify("debug: id = {}".format(me._id))

	notify("{} / {} / {} / {} / {} / {}".format(fireCounterValue, iceCounterValue, windCounterValue, earthCounterValue, lightningCounterValue, waterCounterValue))
	notify("{} plays {} to the table.".format(me, card))
	
	me.counters["Fire CP"].value = 0
	me.counters["Ice CP"].value = 0
	me.counters["Wind CP"].value = 0
	me.counters["Earth CP"].value = 0
	me.counters["Lightning CP"].value = 0
	me.counters["Water CP"].value = 0
#	me.counters["Light CP"].value = 0
#	me.counters["Dark CP"].value = 0

def discardThisCard(card, x = 0, y = 0):
#	whisper("Function is named discardThisCard")
	mute()
	card.moveTo(me.piles["Break Zone"])
	notify("{} discards {} to the Break Zone.".format(me, card))
	
def discardAndGainCP(card, x = 0, y = 0):
#	whisper("Function is named discardAndGainCP")
	mute()
	cardElement = card.Element
	if cardElement == "Light" or cardElement == "Dark":
		whisper("You cannot discard Light or Dark cards for CP.")
		playErrorSound()
		return
	
	discardThisCard(card, x, y)
	if cardElement == "Fire":
		me.counters["Fire CP"].value = me.counters["Fire CP"].value + 2
	elif cardElement == "Ice":
		me.counters["Ice CP"].value = me.counters["Ice CP"].value + 2
	elif cardElement == "Wind":
		me.counters["Wind CP"].value = me.counters["Wind CP"].value + 2
	elif cardElement == "Earth":
		me.counters["Earth CP"].value = me.counters["Earth CP"].value + 2
	elif cardElement == "Lightning":
		me.counters["Lightning CP"].value = me.counters["Lightning CP"].value + 2
	elif cardElement == "Water":
		me.counters["Water CP"].value = me.counters["Water CP"].value + 2
	notify("{} gains two {} CP.".format(me, cardElement))

#---------------------------------------------------------------------------
# Player - Hand - Hand (groupaction)
#---------------------------------------------------------------------------

def discardRandomCard(group, x = 0, y = 0):
#	whisper("Function is named discardRandomCard")
	mute()
	if len(group) == 0:
		whisper("You have no cards in your hand to discard.")
		playErrorSound()
		return
	card = group.random()
	card.moveTo(me.piles["Break Zone"])
	notify("{} randomly discards {} to the Break Zone.".format(me, card))
	
def discardManyRandomCards(group, x = 0, y = 0):
#	whisper("Function is named discardManyRandomCards")
	mute()
	
	if len(group) == 0:
		whisper("You have no cards in your hand to discard.")
		playErrorSound()
		return
	
	askNum = askInteger("How many cards to discard?", 2)
	if askNum < 1:
		whisper("You have to discard at least one card.")
		playErrorSound()
		return
	
	count = 0
	for index in range(0, askNum):
		discardRandomCard(group, x, y)
		count += 1
		if len(group) == 0: 
			break
	notify("{} discarded {} cards total.".format(me, count))
	
def sortHand(group, x = 0, y = 0):
#	whisper("Function is named sortHand")
	mute()
	handSize = len(group)
	if handSize < 2:
		whisper("You can't sort a hand with less than two cards in it.")
		playErrorSound()
		return
		
	arrayOfCards = [None] * handSize
	for index in range(0, handSize):
		arrayOfCards[index] = group[index]
	arrayOfCards.sort(sortingFunction)
	
	for index in range(0, handSize):
		arrayOfCards[index].moveTo(me.piles["Removed From Game"])
	for index in range(0, handSize):
		arrayOfCards[index].moveTo(me.hand)
		
def drawInitial(group, x = 0, y = 0):
#	whisper("Function is named drawInitial")
	mute()
	if turnNumber() > 1: 
		playErrorSound()
		return
#	shuffleDeck(me.deck, 0, 0)
	for index in range(0, 5):
		me.deck.shuffle()
	notify("{} shuffles their deck.".format(me))
	drawManyCards(me.deck, 0, 0, 5)
		
def mulliganHand(group, x = 0, y = 0):
#	whisper("Function is named mulliganHand")
	mute()
	if turnNumber() > 1: 
		playErrorSound()
		return
	askNum = askChoice("Do you really want to mulligan?", ["Yes", "No"])
	if askNum != 1:
		return
		
	notify("{} takes a mulligan, placing their current hand on the bottom of their deck".format(me))
	for card in group:
		card.moveToBottom(me.deck)
	drawManyCards(me.deck, x, y, 5)

#---------------------------------------------------------------------------
# Player - Deck - Deck (groupaction)
#---------------------------------------------------------------------------

def drawCard(group, x = 0, y = 0):
#	whisper("Function is named drawCard")
	mute()
	if len(group) == 0:
		whisper("Your deck is empty.")
		playErrorSound()
		return
	group[0].moveTo(me.hand)
	notify("{} draws a card.".format(me))
	
def drawManyCards(group, x = 0, y = 0, numberOfCards = None):
#	whisper("Function is named drawManyCards")
	mute()
	if len(group) == 0:
		whisper("Your deck is empty.")
		playErrorSound()
		return
	
	askNum = numberOfCards
	if askNum == None:
		askNum = askInteger("How many cards to draw?", 2)
		if askNum < 1:
			whisper("You have to draw at least one card.")
			playErrorSound()
			return
		
	count = 0
	for index in range(0, askNum):
		group[0].moveTo(me.hand)
		count += 1
		if len(group) == 0:
			break
	notify("{} draws {} card(s).".format(me, count))
	
def millManyCards(group, x = 0, y = 0):
#	whisper("Function is named millManyCards")
	mute()
	if len(group) == 0:
		whisper("Your deck is empty.")
		playErrorSound()
		return
	
	askNum = askInteger("How many cards to discard from the deck?", 2)
	if askNum < 1:
		whisper("You have to discard at least one card from the deck.")
		playErrorSound()
		return
		
	count = 0
	for index in range(0, askNum):
		breakCard = group[0]
		breakCard.moveTo(me.piles["Break Zone"])
		notify("{} discards {} from the top of their deck to the Break Zone.".format(me, breakCard))
		count += 1
		if len(group) == 0:
			break
	notify("{} discarded {} card(s) total.".format(me, count))
	
def placeCardIntoDamageZone(group, x = 0, y = 0):
#	whisper("Function is named placeCardIntoDamageZone")
	mute()
	if len(group) == 0:
		whisper("Your deck is empty.")
		playErrorSound()
		return

	notify("{} takes 1 damage.".format(me))
	damageCard = group[0]
	damageCard.moveTo(me.piles["Damage Zone"])
	notify("{} places {} from the top of their deck into the Damage Zone.".format(me, damageCard))
	me.counters["Damage Taken"].value = len(me.piles["Damage Zone"])
	
	if len(me.piles["Damage Zone"]) == 7:
		notify("{} has taken 7 damage!".format(me))
		notify("{} wins!".format(getActivePlayer()))
	
	if damageCard.CanUseEX == "Yes":
		notify("{} has triggered an EX Burst!".format(damageCard))
	
def shuffleDeck(group, x = 0, y = 0):
#	whisper("Function is named shuffleDeck")
	mute()
	group.shuffle()
	notify("{} shuffles their deck.".format(me))

#---------------------------------------------------------------------------
# Player - Break Zone - Break Zone (groupaction)
#---------------------------------------------------------------------------

def shuffleBreakZoneBackIntoDeck(group, x = 0, y = 0):
	whisper("Function is named shuffleBreakZoneBackIntoDeck")

#---------------------------------------------------------------------------
# Extra
#---------------------------------------------------------------------------

def getActivePlayer():
	if players[0].isActivePlayer == True:
		return players[0]
	else:
		return players[1]
		
def getInactivePlayer():
	if players[0].isActivePlayer == False:
		return players[0]
	else:
		return players[1]

def sortingFunction(card1, card2):
	card1Element = card1.Element
	card1ElementValue = 0
	if card1Element == "Fire": card1ElementValue = 1
	elif card1Element == "Ice": card1ElementValue = 2
	elif card1Element == "Wind": card1ElementValue = 3
	elif card1Element == "Earth": card1ElementValue = 4
	elif card1Element == "Lightning": card1ElementValue = 5
	elif card1Element == "Water": card1ElementValue = 6
	elif card1Element == "Light": card1ElementValue = 7
	elif card1Element == "Dark": card1ElementValue = 8
	
	card2Element = card2.Element
	card2ElementValue = 0
	if card2Element == "Fire": card2ElementValue = 1
	elif card2Element == "Ice": card2ElementValue = 2
	elif card2Element == "Wind": card2ElementValue = 3
	elif card2Element == "Earth": card2ElementValue = 4
	elif card2Element == "Lightning": card2ElementValue = 5
	elif card2Element == "Water": card2ElementValue = 6
	elif card2Element == "Light": card2ElementValue = 7
	elif card2Element == "Dark": card2ElementValue = 8
	
	if card1ElementValue > card2ElementValue:
		return 1
	elif card1ElementValue < card2ElementValue:
		return -1
	
	card1CP = card1.CP
	card2CP = card2.CP
	if card1CP > card2CP:
		return 1
	elif card1CP < card2CP:
		return -1
		
	card1Name = card1.name
	card2Name = card2.name
	if card1Name > card2Name:
		return 1
	elif card1Name < card2Name:
		return -1
	else:
		return 0
		
def dealDamage(card, amountOfDamage):
#	whisper("Function is named dealDamage")
	mute()
	
	card.markers[DamageMarker] = amountOfDamage
	
	if amountOfDamage == 0:
		notify("{} is healed of all damage.".format(card))
	else:
		notify("{} is at {} damage.".format(card, amountOfDamage))

def addPower(card, amountOfPower):
#	whisper("Function is named amountOfPower")
	mute()
	
	card.markers[BoostMarker] = amountOfPower
	
#	if amountOfPower > 0:
#		notify("{} has {} extra power.".format(card, amountOfPower))
	notify("{} has {} extra power.".format(card, amountOfPower))
		
def playErrorSound():
	playSound("error")
	
def fixCardsPlayingOnWrongSide(group, x = 0, y = 0):
	mute()
	playMode = getGlobalVariable("PLAY_MODE")
	if playMode == "Default":
		setGlobalVariable("PLAY_MODE", "Fixed")
	else:
		setGlobalVariable("PLAY_MODE", "Default")
		
	newPlayMode = getGlobalVariable("PLAY_MODE")
	notify("The function for playing cards to the field is in {} state.".format(newPlayMode))
	if playMode == "Default":
		notify("If your cards were being played to the TOP of the table (the wrong field), they should now play to the BOTTOM of the table (the right field).")