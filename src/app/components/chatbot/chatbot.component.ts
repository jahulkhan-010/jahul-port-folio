import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

interface Message {
  text: string;
  isUser: boolean;
  timestamp: Date;
}

@Component({
  selector: 'app-chatbot',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chatbot.component.html',
  styleUrl: './chatbot.component.scss'
})
export class ChatbotComponent {
  isOpen = false;
  messages: Message[] = [];
  userInput = '';
  isTyping = false;

  private apiUrl = environment.apiUrl; // Use environment-based URL
  private healthUrl = environment.production ?
    'https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot/health' :
    'http://localhost:5001/api/health';
  private usePythonBackend = false;

  constructor(private http: HttpClient) {
    // Check if Python backend is available
    this.checkBackendConnection();

    // Welcome message
    this.messages.push({
      text: "Hi! I'm Jahul's AI Assistant. I can answer questions about his experience, skills, and projects. How can I help you?",
      isUser: false,
      timestamp: new Date()
    });
  }

  private checkBackendConnection(): void {
    this.http.get(this.healthUrl).subscribe({
      next: () => {
        this.usePythonBackend = true;
        console.log('✅ Python ML backend is connected and ready!');
      },
      error: () => {
        this.usePythonBackend = false;
        console.warn('⚠️ Python backend not available. Using fallback responses.');
        console.log('To enable ML-powered responses, run: cd chatbot-backend && ./start.sh');
      }
    });
  }

  toggleChat(): void {
    this.isOpen = !this.isOpen;
  }

  sendMessage(): void {
    if (!this.userInput.trim()) return;

    // Add user message
    this.messages.push({
      text: this.userInput,
      isUser: true,
      timestamp: new Date()
    });

    const userQuestion = this.userInput;
    this.userInput = '';
    this.isTyping = true;

    // Call backend API (will be implemented)
    this.getBotResponse(userQuestion);
  }

  private getBotResponse(question: string): void {
    console.log('📤 Sending question to backend:', question);
    console.log('🔗 API URL:', this.apiUrl);

    // Try to connect to Python ML backend
    this.http.post<{response: string, status: string}>(this.apiUrl, { question }).subscribe({
      next: (data) => {
        console.log('✅ Received response from Python ML backend:', data.response);
        this.messages.push({
          text: data.response + ' (ML)',
          isUser: false,
          timestamp: new Date()
        });
        this.isTyping = false;
        this.scrollToBottom();
      },
      error: (err) => {
        console.warn('⚠️ Python backend not available, using fallback responses');
        console.log('Error details:', err);
        console.log('💡 To enable ML: cd chatbot-backend && ./start.sh');

        // Fallback to mock responses if backend is not running
        setTimeout(() => {
          const response = this.getMockResponse(question);
          this.messages.push({
            text: response + ' (Fallback)',
            isUser: false,
            timestamp: new Date()
          });
          this.isTyping = false;
          this.scrollToBottom();
        }, 800);
      }
    });
  }

  private getMockResponse(question: string): string {
    const q = question.toLowerCase();
    
    if (q.includes('experience') || q.includes('work')) {
      return "Jahul has 4+ years of experience as an Angular Developer. He's currently a Senior Frontend Developer at V2F Technology since May 2023, previously worked at IMG Global Infotech and Success Ladder Technologies.";
    } else if (q.includes('skill') || q.includes('technology')) {
      return "Jahul is skilled in Angular 19, TypeScript, JavaScript, RxJS, NgRx, SCSS, Material Design, PrimeNG, RESTful APIs, and more. He specializes in building enterprise-scale applications.";
    } else if (q.includes('project') || q.includes('visa2fly')) {
      return "Jahul led the development of Visa2Fly, a comprehensive visa application platform serving 500,000+ users with 99.3% approval rate. He also integrated 24+ white-label partners including IndiGo, SpiceJet, and ixigo.";
    } else if (q.includes('contact') || q.includes('email')) {
      return "You can reach Jahul at jahul.khan@visa2fly.com or jahulkhan010@gmail.com. You can also connect on LinkedIn or GitHub through the links on this portfolio.";
    } else if (q.includes('education')) {
      return "Jahul is an experienced Angular developer with strong foundation in web development, specializing in enterprise applications and modern frontend technologies.";
    } else {
      return "I can help you learn about Jahul's work experience, technical skills, projects like Visa2Fly, or how to contact him. What would you like to know?";
    }
  }

  private scrollToBottom(): void {
    setTimeout(() => {
      const chatMessages = document.querySelector('.chat-messages');
      if (chatMessages) {
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    }, 100);
  }

  handleKeyPress(event: KeyboardEvent): void {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.sendMessage();
    }
  }
}
