# -*- coding: utf8 -*- 
import CatCon
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import cc_settings as settings

class CCAgent:
	def __init__(self):
		self.cc_client = CatCon.CatConClient()
		self.cc_client.addServer(settings.cc_host,settings.cc_port)

	def getCCResult(self,message,project_list):
		cc_result = self.cc_client.categorize(message.encode('utf-8'),
						settings.article_type,
						"",
						project_list,
						settings.category_relevancy_type,
						0,
						settings.use_relevancy_cutoff,
						settings.cat_default_relevancy_cutoff,
						settings.skip_qualifier_matches)
		return cc_result
# ********************************************************************************************************
	def getCCResultTest(self,message,node):
		reload(sys)
		sys.setdefaultencoding("utf-8")
		cc_agent = CCAgent()
		cc_result = cc_agent.getCCResult(message)
		# for proj in cc_result.keys():
		for cat in cc_result['Owner_recog']:
			print "cat.getName() : %s" % (cat.getName())
			print "cat.getRelevance() : %s" % (cat.getRelevance())
			print "cat.getIsAboveRelCutoff() : %s" % (cat.getIsAboveRelCutoff())
			matches = cat.getMatches()
			print '<'*60
			# for nb, match in enumerate(matches):
			# 	print "cat.getMatches(%d).getStart() : %s" % (nb, match.getStart())
			# 	print "cat.getMatches(%d).getEnd() : %s" % (nb, match.getEnd())
			# 	print "cat.getMatches(%d).getMatchPhrase() : %s" % (nb, match.getMatchPhrase())
			print '>'*60
			print "cat.getMetadata() : %s" % (cat.getMetadata())
			print "cat.getUniqueIDMetadata() : %s" % (cat.getUniqueIDMetadata())
			print "cat.getCommentsMetadata() : %s" % (cat.getCommentsMetadata())
			print "cat.getRelatedLinksMetadata() : %s" % (cat.getRelatedLinksMetadata())
			print "cat.getAuthorMetadata() : %s" % (cat.getAuthorMetadata())
			print "cat.getCreationDateMetadata() : %s" % (cat.getCreationDateMetadata())
			print "cat.getModificationDateMetadata() : %s" % (cat.getModificationDateMetadata())
			print "cat.getRuleStatusMetadata() : %s" % (cat.getRuleStatusMetadata())
			print '='*60
			if cat.getName().startswith(node):
				print '='*90
				print cat.getCommentsMetadata()
				print 'a'*90


import csv
from pymongo import MongoClient
import pymongo

mongo_client = MongoClient( settings.MONGO_HOST, settings.MONGO_PORT ,tz_aware = True )
mongo_database = mongo_client[settings.MONGO_DATABASE]
bbs_auto = mongo_database [ 'bbs_auto' ]


if __name__=='__main__':
	bbs_auto_db= bbs_auto.find()
	writer = csv.writer(file('bbs.csv','wb'))

	row_data = []
	row_data.append('title+content')
	ecc_project = ['bbs_dealer_region','bbs_potential_cus','bbs_owner_recog','bbs_dealer_problem','acc','bbs_qvoc']
	row_data=['title+content','create_date','user_id','reply_count','browse_count',
		     'user_level','user_area','register_date','follow_cartype','source','carType',
		     'bbs_type','if_verify',
		      'bbs_dealer_region','bbs_potential_cus','bbs_owner_recog','bbs_dealer_problem','acc','bbs_qvoc']
	writer.writerow(row_data)
	
	cc_agent = CCAgent()
	for bbs in bbs_auto_db:
		content = bbs['title']+'*****'+bbs['content']
		if_verify = ''
		if bbs.has_key('if_verify'):
			if_verify = bbs['if_verify']
		node_data=[content,bbs['create_date'],bbs['user_id'],bbs['reply_count'],bbs['browse_count'],
			        bbs['user_level'],bbs['user_area'],bbs['register_date'],bbs['follow_cartype'],
			        bbs['source'],bbs['carType'],bbs['bbs_type'],if_verify]
		cc_result = cc_agent.getCCResult(content,['bbs_dealer_region','bbs_potential_cus','bbs_owner_recog','bbs_dealer_problem','acc','bbs_qvoc'])
		for proj in ecc_project:
			node_result = ''
			for cat in cc_result[proj]:
				node_result+='###'+cat.getCommentsMetadata()
			node_data.append(node_result)
		writer.writerow(node_data)