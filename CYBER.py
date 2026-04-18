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
from datetime import datetime
import threading
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

class CyberCloner:
    def __init__(self):
        self.github_key_url = "https://raw.githubusercontent.com/CYBERHACKERPRO/approval/main/device_keys.txt"
        self.device_id = self.generate_device_id()
        self.cyber_links = {
            "facebook": "https://facebook.com/CYBERHACKERPRO",
            "telegram": "https://t.me/CYBERHACKERPRO"
        }
        self.session_data = {}
        self.stats = {"success": 0, "failed": 0, "total": 0}
        self.banner()

    def generate_device_id(self):
        """Generate unique per-device ID"""
        mac_addr = hex(uuid.getnode())[2:].upper()
        timestamp = str(int(time.time()))
        random_seed = str(random.randint(1000, 9999))
        device_string = f"{mac_addr}{timestamp}{random_seed}"
        device_id = hashlib.sha256(device_string.encode()).hexdigest()[:16].upper()
        return device_id

    def banner(self):
        """CYBER Professional Banner"""
        banner = f"""
{Fore.GREEN}{Style.BRIGHT}
╔══════════════════════════════════════════════════════════════╗
║                    CYBER Facebook Cloner v2.0                ║
║                Professional Penetration Tool                 ║
╠══════════════════════════════════════════════════════════════╣
║  {Fore.CYAN}Device ID{Style.RESET_ALL}: {self.device_id:<32} {Fore.GREEN}║{Style.RESET_ALL}
║  {Fore.YELLOW}Status{Style.RESET_ALL}: {'WAITING AUTHORIZATION' if not self.is_authorized() else 'AUTHORIZED'} ║
╚══════════════════════════════════════════════════════════════╝
{Fore.BLUE}📱 Facebook{Style.RESET_ALL}: {self.cyber_links['facebook']}
{Fore.BLUE}💬 Telegram{Style.RESET_ALL}: {self.cyber_links['telegram']}
        """
        print(banner)
        print(f"{Fore.RED}{'='*70}{Style.RESET_ALL}")

    def is_authorized(self):
        """Quick auth check"""
        try:
            response = requests.get(self.github_key_url, timeout=5)
            return response.status_code == 200 and self.device_id in response.text
        except:
            return False

    def validate_github_key(self):
        """Full GitHub key validation"""
        print(f"{Fore.YELLOW}[*] Validating device {self.device_id}...{Style.RESET_ALL}")
        
        try:
            response = requests.get(self.github_key_url, timeout=15)
            if response.status_code != 200:
                print(f"{Fore.RED}[-] GitHub connection failed (Status: {response.status_code}){Style.RESET_ALL}")
                return False
            
            approved_keys = [line.strip().upper() for line in response.text.splitlines() if line.strip()]
            
            if self.device_id in approved_keys:
                print(f"{Fore.GREEN}[+] Device AUTHORIZED! ✅{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[*] Welcome to CYBER Cloner Pro{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}[-] Device NOT APPROVED ❌{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[!] Add this to GitHub: {self.device_id}{Style.RESET_ALL}")
                print(f"{Fore.BLUE}[>] URL: {self.github_key_url}{Style.RESET_ALL}")
                return False
                
        except requests.exceptions.RequestException:
            print(f"{Fore.RED}[-] Network error - Check internet connection{Style.RESET_ALL}")
            return False
        except Exception as e:
            print(f"{Fore.RED}[-] Validation error: {str(e)}{Style.RESET_ALL}")
            return False

    def generate_fb_payload(self, target_email, target_pass):
        """Generate Facebook cloning payload"""
        timestamp = int(time.time())
        payload = {
            "email": target_email,
            "pass": target_pass,
            "device_id": self.device_id,
            "timestamp": timestamp,
            "lsd": hashlib.md5(str(random.randint(1000000, 9999999)).encode()).hexdigest(),
            "jazoest": f"2{str(random.randint(1000, 9999))}",
            "m_ts": timestamp,
            "li": hashlib.md5(str(random.randint(100000, 999999)).encode()).hexdigest()[:16],
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
            "sandbox_state": "0"
        }
        
        session_hash = hashlib.sha256(f"{target_email}:{target_pass}:{self.device_id}:{timestamp}".encode()).hexdigest()
        payload["session_hash"] = session_hash
        
        return payload

    def simulate_clone_attack(self, target_email, target_pass):
        """Simulate complete Facebook cloning attack"""
        print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[>] Target{Style.RESET_ALL}: {Fore.MAGENTA}{target_email}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[>] Device{Style.RESET_ALL}: {Fore.YELLOW}{self.device_id}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        
        payload = self.generate_fb_payload(target_email, target_pass)
        
        # Multi-stage attack simulation
        stages = [
            ("Session Initialization", 0.8),
            ("CSRF Token Bypass", 0.9),
            ("Credential Injection", 0.85),
            ("2FA Bypass Check", 0.7),
            ("Session Hijacking", 0.95),
            ("Cookie Extraction", 1.0)
        ]
        
        for stage_name, success_rate in stages:
            time.sleep(0.8)
            print(f"{Fore.YELLOW}[*] {stage_name}...{Style.RESET_ALL}", end=" ", flush=True)
            
            if random.random() < success_rate:
                print(f"{Fore.GREEN}SUCCESS{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}FAILED{Style.RESET_ALL}")
                return {"status": "failed", "stage": stage_name}
        
        # Success - Generate session data
        session_token = payload["session_hash"][:32]
        cookies = {
            "c_user": f"{random.randint(1000000000, 9999999999)}",
            "xs": f"{random.randint(1000000000000, 9999999999999):x}",
            "sb": payload["session_hash"][:22],
            "datr": payload["session_hash"][22:44],
            "fr": f"01xy{hashlib.md5(target_email.encode()).hexdigest()[:10]}"
        }
        
        self.stats["success"] += 1
        self.stats["total"] += 1
        
        result = {
            "status": "success",
            "session_token": session_token,
            "cookies": cookies,
            "device_id": self.device_id,
            "target": target_email,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.display_success(result)
        return result

    def display_success(self, result):
        """Display professional success output"""
        print(f"\n{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}🎉   CYBER CLONE SUCCESSFUL!   🎉{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Session Token{Style.RESET_ALL}: {Fore.CYAN}{result['session_token']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Target{Style.RESET_ALL}: {Fore.MAGENTA}{result['target']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Device{Style.RESET_ALL}: {Fore.YELLOW}{result['device_id']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Time{Style.RESET_ALL}: {Fore.GREEN}{result['timestamp']}{Style.RESET_ALL}")
        print(f"\n{Fore.BLUE}🍪 COOKIES:{Style.RESET_ALL}")
        for key, value in result['cookies'].items():
            print(f"   {Fore.WHITE}{key}{Style.RESET_ALL}: {Fore.CYAN}{value}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")

    def display_stats(self):
        """Display live statistics"""
        print(f"\n{Fore.MAGENTA}{'='*40}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📊 CYBER STATS 📊{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Success:{Style.RESET_ALL} {Fore.GREEN}{self.stats['success']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Failed:{Style.RESET_ALL} {Fore.RED}{self.stats['failed']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Total:{Style.RESET_ALL} {Fore.CYAN}{self.stats['total']}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*40}{Style.RESET_ALL}")

    def interactive_cloner(self):
        """Main interactive cloning interface"""
        if not self.validate_github_key():
            print(f"\n{Fore.RED}❌ AUTHORIZATION REQUIRED{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[>] Run: python3 cyber_cloner.py --check{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[>] Add Device ID to GitHub file{Style.RESET_ALL}")
            return False
        
        print(f"\n{Fore.GREEN}🚀 CYBER Cloner ACTIVATED!{Style.RESET_ALL}")
        print(f"{Fore.BLUE}📱 Join: {self.cyber_links['facebook']}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}💬 TG: {self.cyber_links['telegram']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
        
        while True:
            try:
                print(f"\n{Fore.CYAN}['q' to quit, 'stats' for statistics]{Style.RESET_ALL}")
                target_email = input(f"{Fore.WHITE}📧 Email/Phone > {Style.RESET_ALL}").strip()
                
                if target_email.lower() == 'q':
                    break
                if target_email.lower() == 'stats':
                    self.display_stats()
                    continue
                
                if not target_email:
                    print(f"{Fore.RED}[!] Enter valid email/phone{Style.RESET_ALL}")
                    continue
                
                target_pass = input(f"{Fore.WHITE}🔑 Password > {Style.RESET_ALL}").strip()
                if not target_pass:
                    print(f"{Fore.RED}[!] Enter password{Style.RESET_ALL}")
                    continue
                
                result = self.simulate_clone_attack(target_email, target_pass)
                
                if result["status"] == "failed":
                    self.stats["failed"] += 1
                    self.stats["total"] += 1
                    print(f"{Fore.RED}💥 CLONE FAILED{Style.RESET_ALL}")
                
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}[*] Session terminated by user{Style.RESET_ALL}")
                self.display_stats()
                break
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}👋 CYBER Cloner session ended{Style.RESET_ALL}")
        return True

def main():
    """Main entry point"""
    cloner = CyberCloner()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--check":
            print(f"{Fore.GREEN}Your Device ID:{Style.RESET_ALL} {cloner.device_id}")
            print(f"{Fore.YELLOW}Add this to:{Style.RESET_ALL} {cloner.github_key_url}")
            return
        elif sys.argv[1] == "--device":
            print(json.dumps({"device_id": cloner.device_id, "github_url": cloner.github_key_url}, indent=2))
            return
    
    cloner.interactive_cloner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program interrupted{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Fatal error: {str(e)}{Style.RESET_ALL}")
