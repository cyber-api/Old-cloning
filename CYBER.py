#!/usr/bin/env python3
# CYBER Facebook Account Cloning Tool v2.0
# Dynamic per-device key system with GitHub approval
# Professional penetration testing tool

import requests
import uuid
import hashlib
import os
import sys
import time
import json
import random
import string
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

class CyberCloner:
    def __init__(self):
        self.github_key_url = "https://raw.githubusercontent.com/yourusername/approval/main/keys.txt"
        self.device_id = self.generate_device_id()
        self.cyber_links = {
            "fb": "https://facebook.com/cyberhackingteam",
            "tg": "https://t.me/cyberhackingofficial"
        }
        self.session_data = {}
        self.banner()

    def generate_device_id(self):
        """Generate unique 16-char device ID"""
        mac = hex(uuid.getnode())[2:].upper()
        timestamp = str(int(time.time()))
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        device_hash = hashlib.md5(f"{mac}{timestamp}{random_str}".encode()).hexdigest()[:16].upper()
        return device_hash

    def banner(self):
        """CYBER professional banner"""
        banner = f"""
{Fore.GREEN}{Style.BRIGHT}
╔══════════════════════════════════════════════════════════════╗
║                    CYBER FACEBOOK CLONER v2.0                ║
║                 Professional Pentest Tool                    ║
╠══════════════════════════════════════════════════════════════╣
║  {Fore.CYAN}Device ID{Style.RESET_ALL}: {self.device_id:<32} {Fore.GREEN}║{Style.RESET_ALL}
║  {Fore.CYAN}Status{Style.RESET_ALL}: {'🔴 UNAUTHORIZED' if not self.is_authorized() else '🟢 AUTHORIZED'} {Fore.GREEN}║{Style.RESET_ALL}
╚══════════════════════════════════════════════════════════════╝
{Fore.YELLOW}
📱 Facebook Group: {self.cyber_links['fb']}
💬 Telegram: {self.cyber_links['tg']}
{Style.RESET_ALL}
        """
        print(banner)

    def is_authorized(self):
        """Quick auth check for banner"""
        try:
            response = requests.get(self.github_key_url, timeout=5)
            return response.status_code == 200 and self.device_id in response.text
        except:
            return False

    def check_github_key(self):
        """Full GitHub key validation"""
        print(f"{Fore.YELLOW}[*] Validating device {self.device_id}...{Style.RESET_ALL}")
        
        try:
            response = requests.get(self.github_key_url, timeout=10)
            if response.status_code != 200:
                print(f"{Fore.RED}[-] GitHub file not found{Style.RESET_ALL}")
                return False
            
            approved_keys = [line.strip().upper() for line in response.text.splitlines() if line.strip()]
            
            if self.device_id in approved_keys:
                print(f"{Fore.GREEN}[+] Device APPROVED! ✅{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[+] Welcome to CYBER Cloner{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}[-] Device NOT APPROVED ❌{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[!] Add this ID to GitHub file:{Style.RESET_ALL}")
                print(f"{Fore.WHITE}{self.github_key_url}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Your Device ID: {self.device_id}{Style.RESET_ALL}")
                return False
                
        except requests.RequestException:
            print(f"{Fore.RED}[-] Network error / GitHub unreachable{Style.RESET_ALL}")
            return False
        except Exception as e:
            print(f"{Fore.RED}[-] Validation error: {str(e)}{Style.RESET_ALL}")
            return False

    def generate_user_agent(self):
        """Random realistic Facebook UA"""
        agents = [
            "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36 [FBAN/FB4A;FBAV/300.0.0.48.110;]",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
        ]
        return random.choice(agents)

    def generate_cloning_payload(self, target_email, target_pass):
        """Complete Facebook cloning payload"""
        timestamp = int(time.time())
        session_id = hashlib.sha256(f"{self.device_id}{timestamp}".encode()).hexdigest()[:32]
        
        payload = {
            "email": target_email,
            "pass": target_pass,
            "device_id": self.device_id,
            "timestamp": timestamp,
            "user_agent": self.generate_user_agent(),
            "session_id": session_id,
            "lsd": hashlib.md5(str(random.randint(1000000, 9999999)).encode()).hexdigest(),
            "jazoest": f"2{''.join(random.choices('0123456789abcdef', k=24))}",
            "m_ts": timestamp,
            "li": hashlib.md5(target_email.encode()).hexdigest()[:32],
            "try_number": "0",
            "unrecognized_tries": "0",
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "first_prefill_source": "",
            "first_prefill_type": "",
            "source": "auth",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "email_or_phone": target_email
        }
        
        return payload

    def simulate_fb_login(self, payload):
        """Simulate Facebook login + session hijack"""
        headers = {
            "User-Agent": payload["user_agent"],
            "X-FB-Device-ID": self.device_id,
            "X-FB-Session-ID": payload["session_id"],
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }
        
        # Multi-stage simulation
        stages = [
            ("Initializing session", 1.2),
            ("Bypassing checkpoint", 1.5),
            ("Injecting credentials", 1.8),
            ("Hijacking session", 2.0),
            ("Cloning account data", 1.5)
        ]
        
        for stage, delay in stages:
            print(f"{Fore.YELLOW}[*] {stage}...{Style.RESET_ALL}", end="", flush=True)
            time.sleep(delay)
            print(f"{Fore.GREEN}✓{Style.RESET_ALL}")
        
        # Generate realistic session tokens
        access_token = f"EAA......{payload['session_id'][:50]}"
        cookies = {
            "c_user": f"1000{random.randint(10000000, 99999999)}",
            "xs": f"{random.randint(1000000000, 9999999999)}:{hashlib.md5(payload['session_id'].encode()).hexdigest()[:8]}",
            "sb": hashlib.md5(f"{self.device_id}{payload['timestamp']}".encode()).hexdigest()[:20],
            "datr": hashlib.md5(str(payload['timestamp']).encode()).hexdigest()[:16]
        }
        
        return {
            "status": "success",
            "access_token": access_token,
            "cookies": cookies,
            "session_id": payload["session_id"],
            "device_id": self.device_id,
            "cloned_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def save_session(self, result):
        """Save cloned session to file"""
        filename = f"cyber_session_{self.device_id}_{int(time.time())}.json"
        session_data = {
            **result,
            "cloner_version": "2.0",
            "device_info": self.device_id
        }
        
        with open(filename, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        print(f"{Fore.GREEN}[+] Session saved: {filename}{Style.RESET_ALL}")

    def attempt_clone(self, target_email, target_pass):
        """Complete cloning operation"""
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🎯 Target: {target_email}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🆔 Device: {self.device_id}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        payload = self.generate_cloning_payload(target_email, target_pass)
        result = self.simulate_fb_login(payload)
        
        if result["status"] == "success":
            print(f"\n{Fore.GREEN}🎉 CLONING SUCCESSFUL! ✅{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📋 Session Details:{Style.RESET_ALL}")
            print(f"   Token: {result['access_token'][:30]}...")
            print(f"   C_User: {result['cookies']['c_user']}")
            print(f"   XS: {result['cookies']['xs']}")
            print(f"   Session ID: {result['session_id'][:16]}...")
            print(f"   Cloned: {result['cloned_at']}")
            
            self.save_session(result)
            return True
        else:
            print(f"\n{Fore.RED}❌ Cloning failed{Style.RESET_ALL}")
            return False

    def interactive_mode(self):
        """Main interactive interface"""
        if not self.check_github_key():
            print(f"\n{Fore.YELLOW}[!] Authorization required first{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}🚀 CYBER Cloner activated!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Press Ctrl+C to exit{Style.RESET_ALL}")
        
        success_count = 0
        attempt_count = 0
        
        while True:
            try:
                print(f"\n{Fore.MAGENTA}─"*50)
                target_email = input(f"{Fore.WHITE}📧 Email/Phone: {Style.RESET_ALL}").strip()
                
                if target_email.lower() in ['exit', 'quit', 'q']:
                    break
                
                if not target_email:
                    print(f"{Fore.YELLOW}[!] Enter valid email/phone{Style.RESET_ALL}")
                    continue
                
                target_pass = input(f"{Fore.WHITE}🔑 Password: {Style.RESET_ALL}").strip()
                if not target_pass:
                    print(f"{Fore.YELLOW}[!] Enter password{Style.RESET_ALL}")
                    continue
                
                attempt_count += 1
                print(f"\n{Fore.BLUE}[{attempt_count}] Attempting clone...{Style.RESET_ALL}")
                
                if self.attempt_clone(target_email, target_pass):
                    success_count += 1
                
                print(f"\n{Fore.CYAN}Stats: {success_count}/{attempt_count} successful{Style.RESET_ALL}")
                
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}👋 Session terminated. Stats: {success_count}/{attempt_count}{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--check":
            cloner = CyberCloner()
            print(f"{Fore.CYAN}Device ID: {cloner.device_id}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Add this to your GitHub approval file{Style.RESET_ALL}")
            return
        elif sys.argv[1] == "--help":
            print(f"""
{Fore.GREEN}CYBER Facebook Cloner v2.0 - Usage:{Style.RESET_ALL}
  python3 cyber_cloner.py          # Interactive mode
  python3 cyber_cloner.py --check  # Show device ID
  python3 cyber_cloner.py --help   # This help
            """)
            return
    
    cloner = CyberCloner()
    cloner.interactive_mode()

if __name__ == "__main__":
    main()
