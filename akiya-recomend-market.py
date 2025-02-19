class MarketFactors:
    """ 市場環境のデータを保持 """
    def __init__(self, area_type: str, factors: dict, epsilon: float = 0.0):
        """
        :param area_type: "urban" or "rural"
        :param factors: {"population": 値, "distance_from_station": 値, ...} など
        :param epsilon: Potential_score に加算する定数
        """
        self.area_type = area_type
        self.factors = factors
        self.epsilon = epsilon


class MarketPotentialCalculator:
    """ 市場ポテンシャル(Potential_score)を計算 """
    FACTOR_RANGES = {
        "urban": {
            "population": 10000,
            "distance_from_station": 20,
            "tourist": 10000, 
            "household_income": 10000000
        },
        "rural": {
            "population": 5000,
            "distance_from_station": 40,
            "tourist": 300, 
            "household_income": 8000000
        }
    }

    WEIGHTS = {
        "urban": {
            "cafe": {
                "population": 0.3, 
                "distance_from_station": 0.3, 
                "tourist": 0.2, 
                "household_income": 0.2
            },
            "accommodation": {
                "population": 0.2, 
                "distance_from_station": 0.2, 
                "tourist": 0.3, 
                "household_income": 0.3
            },
            "shareAtelier": {
                "population": 0.25, 
                "distance_from_station": 0.25, 
                "tourist": 0.25, 
                "household_income": 0.25
            }
        },
        "rural": {
            "cafe": {
                "population": 0.25, 
                "distance_from_station": 0.25, 
                "tourist": 0.25, 
                "household_income": 0.25
            },
            "accommodation": {
                "population": 0.25, 
                "distance_from_station": 0.25, 
                "tourist": 0.25, 
                "household_income": 0.25
            },
            "shareAtelier": {
                "population": 0.25, 
                "distance_from_station": 0.25, 
                "tourist": 0.25, 
                "household_income": 0.25
            }
        }
    }

    @classmethod
    def _normalize_factor(cls, area_type: str, factor_name: str, value: float) -> float:
        """ 指標を 0～1 に正規化 """
        max_val = cls.FACTOR_RANGES[area_type].get(factor_name, 0)  # 未登録の指標はそのまま
        if factor_name == "distance_from_station":
            return max(0.0, 1.0 - (value / max_val)) if value < max_val else 0.0
        return min(1.0, value / max_val)

    @classmethod
    def calculate(cls, factors: MarketFactors, business_type: str) -> float:
        """ 各指標を正規化し、重み付けして Potential_score を算出 """
        weights = cls.WEIGHTS[factors.area_type].get(business_type, {})
        weighted_sum = sum(weights.get(f, 0) * cls._normalize_factor(factors.area_type, f, v)
                           for f, v in factors.factors.items())
        return weighted_sum + factors.epsilon  # ε を加算


class Business:
    """ 任意の事業の収支を計算 """
    def __init__(self, name: str, initial_investment: int, users: int, unit_price: int, other_revenue: int, costs: dict):
        self.name = name
        self.initial_investment = initial_investment
        self.users = users
        self.unit_price = unit_price
        self.other_revenue = other_revenue
        self.costs = costs

    def calc_monthly_revenue(self, market_score: float = 1.0) -> int:
        """ 市場スコアを考慮した月間売上を算出 """
        return int(self.users * self.unit_price * market_score + self.other_revenue)

    def calc_monthly_cost(self) -> int:
        """ 月間コスト合計を算出 """
        return sum(self.costs.values())

    def calc_monthly_profit(self, monthly_revenue: int, monthly_cost: int) -> int:
        """ 月間利益を算出 """
        return monthly_revenue - monthly_cost

    def calc_profit_ratio(self, monthly_profit: int, monthly_cost: int) -> float:
        """ 利益率(%) を算出 """
        return (monthly_profit / monthly_cost * 100) if monthly_cost else 0.0

    def calc_payback_period(self, monthly_profit: int) -> float:
        """ 投資回収期間(年) を算出 """
        return (self.initial_investment / monthly_profit) / 12 if monthly_profit else float('inf')

    def print_summary(self, market_score: float):
        """ 事業収支を出力 """
        monthly_revenue = self.calc_monthly_revenue(market_score)
        monthly_cost = self.calc_monthly_cost()
        monthly_profit = self.calc_monthly_profit(monthly_revenue, monthly_cost)
        profit_ratio = self.calc_profit_ratio(monthly_profit, monthly_cost)
        payback_period = self.calc_payback_period(monthly_profit)

        print(f"\n===== {self.name} の結果 =====")
        print(f"・市場スコア (Potential) : {market_score:.2f}")
        print(f"・初期投資額             : {self.initial_investment}円")
        print(f"・月間売上               : {monthly_revenue}円")
        print(f"・月間経費               : {monthly_cost}円")
        print(f"・月間利益               : {monthly_profit}円")
        print(f"・収益率                 : {profit_ratio:.1f}%")
        print(f"・回収期間               : {payback_period:.2f}年")


class BusinessManager:
    """ 複数の事業を管理し、市場スコアを適用して収支を計算 """
    def __init__(self, businesses: dict, market_factors: MarketFactors):
        """
        :param businesses: { 
        "cafe": Businessインスタンス, "accommodation": Businessインスタンス, ... }
        :param market_factors: MarketFactors インスタンス
        """
        self.businesses = businesses
        self.market_factors = market_factors

    def run_analysis(self):
        """ すべての事業について市場スコアを適用し、収支分析を実行 """
        for name, business in self.businesses.items():
            market_score = MarketPotentialCalculator.calculate(
                self.market_factors, name)
            business.print_summary(market_score)


# ---------------------------------------------------------
# 実行コード
# ---------------------------------------------------------
if __name__ == "__main__":
    # 調査地点周辺エリアの市場要因 (例: 都市部, 具体的な指標値)
    market_factors = MarketFactors(
        area_type="urban",
        factors={
            "population": 8000, 
            "distance_from_station": 10, 
            "tourist": 5000, 
            "household_income": 7_000_000
        },
        epsilon=0.5
    )

    # 比較対象の事業リスト
    businesses = {
        "cafe": Business(
            name="カフェ",
            initial_investment=30_000_000,
            users=2_500,
            unit_price=1_100,
            other_revenue=50_000,
            costs={
                "人件費": 1_147_500,
                "水道光熱費": 50_000,
                "通信費": 6_000,
                "清掃費": 70_000,
                "消耗品費": 150_000,
                "保険料": 5_000,
                "修繕費": 0, 
                "地代家賃": 150_000,
                "その他経費": 821_500
            }
        ),
        "accommodation": Business(
            name="宿泊施設",
            initial_investment=50_000_000,
            users=200,
            unit_price=12_000,
            other_revenue=50_000,
            costs={
                "人件費": 250_000,
                "水道光熱費": 30_000,
                "通信費": 6_000,
                "清掃費": 70_000,
                "消耗品費": 70_000,
                "保険料": 2_000,
                "修繕費": 0,
                "地代家賃": 200_000,
                "その他経費": 192_000
            },
        ),
        "shareAtelier": Business(
            name="シェアアトリエ",
            initial_investment=10_000_000,
            users=50,
            unit_price=20_000,
            other_revenue=0,
            costs={
                "人件費": 300_000,
                "水道光熱費": 30_000,
                "通信費": 6_000,
                "清掃費": 70_000,
                "消耗品費": 50_000,
                "保険料": 2_000,
                "修繕費": 0,
                "地代家賃": 100_000,
                "その他経費": 100_000
            }
        )
    }

    # 事業計算マネージャーで計算
    manager = BusinessManager(businesses, market_factors)
    manager.run_analysis()
