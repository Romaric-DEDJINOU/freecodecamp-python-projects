class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Méthode pour ajouter un dépôt
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Méthode pour faire un retrait
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True

        return False

    # Méthode pour calculer le solde actuel
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    # Méthode pour transférer de l'argent vers une autre catégorie
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    # Méthode d'aide pour vérifier le solde
    def check_funds(self, amount):
        return amount <= self.get_balance()

    # Méthode spéciale pour l'affichage (le relevé de compte)
    def __str__(self):

        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            # La description est tronquée à 23 caractères et alignée à gauche
            # Le montant est formaté avec 2 décimales et aligné à droite sur 7 caractères
            items += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total





def create_spend_chart(categories):
    withdrawals = []
    for cat in categories:
        # On calcule le total des retraits pour chaque catégorie
        total_cat_withdrawals = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total_cat_withdrawals += item["amount"]
        withdrawals.append(abs(total_cat_withdrawals))

    # On calcule le total des dépenses et les pourcentages
    total_withdrawals = sum(withdrawals)
    percentages = [(w / total_withdrawals * 100 // 10) * 10 for w in withdrawals]

    # 2. Construction de la chaîne de caractères du graphique
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            if p >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # 3. Ajout de la ligne de tirets
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Ajout des noms de catégories à la verticale
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    padded_names = [name.ljust(max_len) for name in names]

    for i in range(max_len):
        chart += "     "
        for name in padded_names:
            chart += name[i] + "  "
        # On ajoute un saut de ligne sauf pour la toute dernière ligne
        if i < max_len - 1:
            chart += "\n"

    return chart
