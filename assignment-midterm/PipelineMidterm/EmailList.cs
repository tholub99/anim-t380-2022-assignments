using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PipelineMidterm
{
    public class EmailList
    {
        string title;
        Dictionary<string, string> emails;
        public EmailList(string configPath)
        {
            title = "Missing";
            emails = new Dictionary<string, string>();
            foreach (string line in File.ReadLines(configPath))
            {
                string[] breakdown = line.Split(",");
                if(breakdown.Length == 1)
                {
                    title = breakdown[0];
                    continue;
                }
                string name = breakdown[0];
                string email = breakdown[1];
                emails.Add(name, email);
            }
        }

        public EmailList(EmailList other)
        {
            this.title = other.title;
            this.emails = new Dictionary<string,string>(other.emails);
        }
        public string GetTitle()
        {
            return title;
        }

        public List<string> GetRecipients()
        {
            return emails.Values.ToList();
        }

        public List<string> GetNames()
        {
            return emails.Keys.ToList();
        }

        public Dictionary<string, string> GetEmailMap()
        {
            return emails;
        }

        public void RemoveEmail(string name)
        {
            emails.Remove(name);
        }

        public void AddEmail(string name, string email)
        {
            emails.Add(name, email);
        }

        public EmailList SaveAsNewConfig(string title, string configDir)
        {
            string[] titleArr =
            {
                title
            };
            string[] emailsArr = emails.Select(x => String.Format("{0},{1}", x.Key, x.Value)).ToArray();
            string[] newConfig = titleArr.Concat(emailsArr).ToArray();
            string newPath = String.Format("{0}\\{1}.ecfg", configDir, title);
            File.WriteAllLines(newPath, newConfig);

            return new EmailList(newPath);
        }
    }
}
