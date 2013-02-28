using System;   
using System.Collections;   
using System.Linq;   
using System.Text;   
using System.IO;  
using System.Text.RegularExpressions; 

namespace Demo{  

	public class FileSummary{
		int filesCount = 0;
		int wordsCount = 0;
		
		public void DoSummary(string filename){
			filesCount += 1;
			wordsCount += GetWordsCount(filename);
		}
		
		public string Output(){
			return string.Format("有{0}个.字数有{1}个.\n", filesCount, wordsCount);
		}
		
		int GetWordsCount(string filename)
		{
			using (StreamReader sr = new StreamReader(filename)){
           		Regex regex = new Regex("\\w+");
            	return regex.Matches(sr.ReadToEnd()).Count;
           	}
    	}
	}
	
	public class SummaryFactory{
		Hashtable summaries = new Hashtable();

		public FileSummary GetFileSummary(string ext){
			if(summaries.Contains(ext)){
				return summaries[ext] as FileSummary;
			}else{
				FileSummary summary = new FileSummary();
				summaries.Add(ext, summary);
				return summary;
			}
		}

		public string Output(){
			string s = "";
			IDictionaryEnumerator en = summaries.GetEnumerator();
			while (en.MoveNext())
			{
      			FileSummary summary = en.Value as FileSummary;
      			s += string.Format("此目录中拥有的{0}文件", en.Key);
				s += summary.Output();
			}
			return s;
		}
	}

	public class Utility{
		SummaryFactory factory = new SummaryFactory();
	
		public string Output(string path){
			string [] AllFile =Directory.GetFiles(path);
			foreach(string filename in AllFile){
				string ext = Path.GetExtension(filename);
				factory.GetFileSummary(ext).DoSummary(filename);
			}
			return string.Format("当前日期是:{0}\n", DateTime.Now)
				+ string.Format("你输入的目录是：{0}\n", path)
				+ factory.Output();
		}
	}

	class Program
	{ 
		static void WriteLog(string pathLogFile, string s){
			using (StreamWriter sw = new StreamWriter(File.Open(pathLogFile, FileMode.Append | FileMode.OpenOrCreate))){
				sw.WriteLine(s);   
			}
		}
		
		static void Main(string[] args){
			try{
				WriteLog(@"/tmp/log.txt", new Utility().Output(@"/tmp/demo"));
			}catch{
				Console.ReadKey();
			}
		 }	
    }
}
