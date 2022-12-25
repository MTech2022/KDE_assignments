#Roll No : 12
#Pincer Search: An algorithm for Maximal Frequent Itemset (MFI) mining
from itertools import combinations

def generateMFCS(MFCS, infrequent_itemsets):
	MFCS = MFCS.copy()

	for infrequent_itemset in infrequent_itemsets:
		for MFCS_itemset in MFCS.copy():
			# If infrequent itemset is a subset of MFCS itemset
			if all(_item in MFCS_itemset for _item in infrequent_itemset):
				MFCS.remove(MFCS_itemset)
				
				for item in infrequent_itemset:
					updated_MFCS_itemset = MFCS_itemset.copy()
					updated_MFCS_itemset.remove(item)

					if not any(all(_item in _MFCS_itemset for _item in updated_MFCS_itemset) for _MFCS_itemset in MFCS):
						MFCS.append(updated_MFCS_itemset)

	return MFCS


def pruneCandidatesUsingMFS(candidate_itemsets, MFS):
	candidate_itemsets = candidate_itemsets.copy()
	for itemset in candidate_itemsets.copy():
		if any(all(_item in _MFS_itemset for _item in itemset) for _MFS_itemset in MFS):
			candidate_itemsets.remove(itemset)
	return candidate_itemsets


def generateCandidateItemsets(level_k, level_frequent_itemsets):
	n_frequent_itemsets = len(level_frequent_itemsets)
	candidate_frequent_itemsets = []

	for i in range(n_frequent_itemsets):
		j = i+1
		while (j<n_frequent_itemsets) and (level_frequent_itemsets[i][:level_k-1] == level_frequent_itemsets[j][:level_k-1]):
			
			candidate_itemset = level_frequent_itemsets[i][:level_k-1] + [level_frequent_itemsets[i][level_k-1]] + [level_frequent_itemsets[j][level_k-1]]
			candidate_itemset_pass = False

			if level_k == 1:
				candidate_itemset_pass = True
				
			elif (level_k == 2) and (candidate_itemset[-2:] in level_frequent_itemsets):
				candidate_itemset_pass = True

			elif all((list(_)+candidate_itemset[-2:]) in level_frequent_itemsets for _ in combinations(candidate_itemset[:-2], level_k-2)):
				candidate_itemset_pass = True
				
			if candidate_itemset_pass:
				candidate_frequent_itemsets.append(candidate_itemset)

			j += 1

	return candidate_frequent_itemsets


def pruneCandidatesUsingMFCS(candidate_itemsets, MFCS):
	candidate_itemsets = candidate_itemsets.copy()
	for itemset in candidate_itemsets.copy():
		if not any(all(_item in _MFCS_itemset for _item in itemset) for _MFCS_itemset in MFCS):
			candidate_itemsets.remove(itemset)
	return candidate_itemsets


def pincer_search(transactions, min_support):
	items = set()
	for transaction in transactions:
		items.update(transaction)
	items = sorted(list(items))
	
	level_k = 1 # The current level number

	level_frequent_itemsets = [] # Level 0: Frequent itemsets
	candidate_frequent_itemsets = [[item] for item in items] # Level 1: Candidate itemsets
	level_infrequent_itemsets = [] # Level 0: Infrequent itemsets

	MFCS = [items.copy()]
	MFS = []

	print("Maximum Frequent Candidate Set(MFCS) = {}".format(MFCS))
	print("Maximal Frequent set(MFS) = {}\n".format(MFS))
	print("------------------------------------------------------------------------------------------------------------")
	while candidate_frequent_itemsets:
		
		print("LEVEL.{}: ".format(level_k))
		print("CANDIDATE_FREQUENT_ITEMSETS.{} = {}".format(level_k, candidate_frequent_itemsets))

		candidate_freq_itemsets_count = [0]*len(candidate_frequent_itemsets)
		MFCS_itemsets_count = [0]*len(MFCS)

		# Step 1: Read the database and count supports for Ck and MFCS
		for transaction in transactions:
			
			for i, itemset in enumerate(candidate_frequent_itemsets):
				if all(_item in transaction for _item in itemset):
					candidate_freq_itemsets_count[i] += 1

			for i, itemset in enumerate(MFCS):
				if all(_item in transaction for _item in itemset):
					MFCS_itemsets_count[i] += 1

		for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_count):
			print(f"{itemset} --> {support}", end=', \n')
		print("`````````````````````````````````````")

		for itemset, support in zip(MFCS, MFCS_itemsets_count):
			print(f"{itemset} --> {support}", end=', \n')
		print("`````````````````````````````````````")

		MFS.extend([itemset for itemset, support in zip(MFCS, MFCS_itemsets_count) if ((support >= min_support) and (itemset not in MFS))])
		print("Maximal Frequent sets(MFS) = {}".format(MFS))

		level_frequent_itemsets = [itemset for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_count) if support >= min_support]
		level_infrequent_itemsets = [itemset for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_count) if support < min_support]

		print("LEVEL.{} = {}".format(level_k, level_frequent_itemsets))
		print("INFREQUENT_ITEMSETS.{} = {}".format(level_k, level_infrequent_itemsets))

		MFCS = generateMFCS(MFCS, level_infrequent_itemsets)
		print("Maximum Frequent Candidate Set(MFCS) = {}".format(MFCS))

		level_frequent_itemsets = pruneCandidatesUsingMFS(level_frequent_itemsets, MFS)
		print("After Pruning: L{} = {}".format(level_k, level_frequent_itemsets))

		candidate_frequent_itemsets = generateCandidateItemsets(level_k, level_frequent_itemsets)
		candidate_frequent_itemsets = pruneCandidatesUsingMFCS(candidate_frequent_itemsets, MFCS)
		print(
			f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Level-{level_k}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		level_k += 1
	return MFS

if __name__ == '__main__':

	print("==============================================================================================================\n"
		  "I.Implement the following algorithms in Python for finding the frequent itemsets\n"
		  "\tii. Pincer Search.\n"
		  "-------------------------------------------------------------------------------------------------------------\n")
	transactions = [
		{1, 5, 6, 8},
		{2, 4, 8},
		{4, 5, 7},
		{2, 3},
		{5, 6, 7},
		{2, 3, 4},
		{2, 6, 7, 9},
		{5},
		{8},
		{3, 5, 7},
		{3, 5, 7},
		{5, 6, 8},
		{2, 4, 6, 7},
		{1, 3, 5, 7},
		{2, 3, 9},
	]

	min_support_count = 3

	MFS = pincer_search(transactions, min_support_count)
	print("Maximal Frequent Sets = {}".format(MFS))

	# Below are some more example
	'''
	transactions = [
		{1, 5, 6, 8},
		{2, 4, 8},
		{4, 5, 7},
		{3},
		{5, 6, 7},
		{2, 3, 4},
		{2, 6, 7, 9},
		{5},
		{8},
		{3, 4, 5, 7},
		{3, 4, 5, 7},
		{5, 6, 8},
		{2, 3, 4, 6, 7},
		{1, 3, 4, 5, 7},
		{2, 3, 9},
	]

	min_support_count = 3
	'''

	'''
	transactions = [
		{1,2,3},
		{3,4},
		{1,2},
		{3,5},
		{2,5}
	]

	min_support_count = 1
	'''
