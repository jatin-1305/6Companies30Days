class Transaction:
    def __init__(self, idx, time, amount, city):
        self.idx = idx
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
    
    def __repr__(self):
        return f"{self.idx}, {self.time}, {self.amount}, {self.city}"

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        customers = defaultdict(list)
        invalid_tx = set()
        
        for transaction_idx in range(len(transactions)):
            name, time, amount, city = transactions[transaction_idx].split(',')
            new_tx = Transaction(transaction_idx, time, amount, city)
            
            if new_tx.amount > 1000:
                invalid_tx.add(new_tx.idx)
            
            if not name in customers:
                customers[name].append(new_tx)
                continue
            
            for tx in customers[name]:
                if (new_tx.city != tx.city) and abs(new_tx.time - tx.time) <= 60:
                    # print(new_tx, " | ", tx)
                    invalid_tx.add(new_tx.idx)
                    invalid_tx.add(tx.idx)
            
            customers[name].append(new_tx)
            
        return [transactions[idx] for idx in invalid_tx]
