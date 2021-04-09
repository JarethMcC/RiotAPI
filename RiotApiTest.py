import urllib.request as request
import json

summonerName = input("Please input your summoner name: ")

def requestSummonerData():
	with request.urlopen("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=RGAPI-b12ee8cf-1ff6-4751-a668-b253d65a6392") as response:
		source = response.read()
		data = json.loads(source)
		return data


def requestRankData(summonerID):
	with request.urlopen("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=RGAPI-b12ee8cf-1ff6-4751-a668-b253d65a6392") as response:
		source = response.read()
		data = json.loads(source)[0]
		return data

def main():
	summonerData = requestSummonerData()
	rankData = requestRankData(summonerData["id"])
	print(summonerData["name"])
	print(rankData["tier"])

main()
