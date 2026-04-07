import { Injectable } from '@angular/core';
import jsPDF from 'jspdf';

@Injectable({
  providedIn: 'root'
})
export class ResumeService {

  constructor() { }

  generateResume(): void {
    const doc = new jsPDF();
    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();
    const margin = 20;
    let yPosition = 20;

    // Helper function to add text with word wrap
    const addText = (text: string, x: number, y: number, maxWidth: number, fontSize: number = 10, isBold: boolean = false) => {
      doc.setFontSize(fontSize);
      doc.setFont('helvetica', isBold ? 'bold' : 'normal');
      const lines = doc.splitTextToSize(text, maxWidth);
      doc.text(lines, x, y);
      return y + (lines.length * fontSize * 0.5);
    };

    // Header - Name and Title
    doc.setFillColor(138, 43, 226); // Purple color
    doc.rect(0, 0, pageWidth, 45, 'F');
    
    doc.setTextColor(255, 255, 255);
    doc.setFontSize(28);
    doc.setFont('helvetica', 'bold');
    doc.text('JAHUL KHAN', pageWidth / 2, 20, { align: 'center' });
    
    doc.setFontSize(14);
    doc.setFont('helvetica', 'normal');
    doc.text('Senior Frontend Developer', pageWidth / 2, 30, { align: 'center' });
    
    doc.setFontSize(10);
    doc.text('jahul.khan@visa2fly.com | Angular Expert | 4+ Years Experience', pageWidth / 2, 38, { align: 'center' });

    yPosition = 55;
    doc.setTextColor(0, 0, 0);

    // Professional Summary
    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(138, 43, 226);
    doc.text('PROFESSIONAL SUMMARY', margin, yPosition);
    yPosition += 8;

    doc.setFontSize(10);
    doc.setFont('helvetica', 'normal');
    doc.setTextColor(0, 0, 0);
    const summary = 'Angular Frontend Developer with 4 years of experience, skilled in building responsive, user-friendly web applications using Angular, TypeScript, and modern UI tools. Proven track record of creating smooth, clean interfaces that balance user needs and business goals. Successfully delivered enterprise-scale applications serving 500,000+ users with 99.3% approval rate.';
    yPosition = addText(summary, margin, yPosition, pageWidth - 2 * margin, 10);
    yPosition += 8;

    // Work Experience
    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(138, 43, 226);
    doc.text('WORK EXPERIENCE', margin, yPosition);
    yPosition += 8;

    // Job 1
    doc.setFontSize(12);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(0, 0, 0);
    doc.text('Senior Frontend Developer', margin, yPosition);
    doc.setFontSize(10);
    doc.setFont('helvetica', 'italic');
    doc.text('May 2023 - Present', pageWidth - margin - 40, yPosition);
    yPosition += 6;

    doc.setFont('helvetica', 'normal');
    doc.text('V2F Technology Private Limited (Visa2Fly)', margin, yPosition);
    yPosition += 6;

    const job1Desc = [
      '• Led development of Visa2Fly platform serving 500,000+ visa applications with 99.3% approval rate',
      '• Architected and implemented 4 enterprise applications: Consumer Platform, B2B Portal, Agent Dashboard, and Admin Portal',
      '• Integrated 24+ white-label partner solutions for leading airlines (IndiGo, SpiceJet, Vistara) and travel platforms',
      '• Implemented AI-powered document validation system and real-time application tracking',
      '• Built multi-tenant architecture supporting custom theming and configurations for each partner',
      '• Optimized application performance resulting in 40% faster load times and improved user experience'
    ];

    job1Desc.forEach(item => {
      doc.setFontSize(9);
      doc.setFont('helvetica', 'normal');
      const lines = doc.splitTextToSize(item, pageWidth - 2 * margin - 10);
      doc.text(lines, margin + 5, yPosition);
      yPosition += lines.length * 4.5;
    });
    yPosition += 4;

    // Job 2
    doc.setFontSize(12);
    doc.setFont('helvetica', 'bold');
    doc.text('Angular Developer', margin, yPosition);
    doc.setFontSize(10);
    doc.setFont('helvetica', 'italic');
    doc.text('May 2022 - May 2023', pageWidth - margin - 40, yPosition);
    yPosition += 6;

    doc.setFont('helvetica', 'normal');
    doc.text('IMG Global Infotech', margin, yPosition);
    yPosition += 6;

    const job2Desc = [
      '• Developed responsive web applications using Angular 14+ and TypeScript',
      '• Collaborated with cross-functional teams to deliver high-quality software solutions',
      '• Implemented RESTful API integrations and state management using RxJS',
      '• Enhanced application performance through code optimization and best practices'
    ];

    job2Desc.forEach(item => {
      doc.setFontSize(9);
      doc.setFont('helvetica', 'normal');
      const lines = doc.splitTextToSize(item, pageWidth - 2 * margin - 10);
      doc.text(lines, margin + 5, yPosition);
      yPosition += lines.length * 4.5;
    });
    yPosition += 4;

    // Job 3
    doc.setFontSize(12);
    doc.setFont('helvetica', 'bold');
    doc.text('Angular Intern', margin, yPosition);
    doc.setFontSize(10);
    doc.setFont('helvetica', 'italic');
    doc.text('Feb 2022 - May 2022', pageWidth - margin - 40, yPosition);
    yPosition += 6;

    doc.setFont('helvetica', 'normal');
    doc.text('Success Ladder Technologies Pvt. Ltd.', margin, yPosition);
    yPosition += 6;

    const job3Desc = [
      '• Learned Angular framework fundamentals and TypeScript programming',
      '• Assisted in developing UI components and implementing responsive designs',
      '• Gained hands-on experience with version control (Git) and agile methodologies'
    ];

    job3Desc.forEach(item => {
      doc.setFontSize(9);
      doc.setFont('helvetica', 'normal');
      const lines = doc.splitTextToSize(item, pageWidth - 2 * margin - 10);
      doc.text(lines, margin + 5, yPosition);
      yPosition += lines.length * 4.5;
    });
    yPosition += 8;

    // Check if we need a new page
    if (yPosition > pageHeight - 60) {
      doc.addPage();
      yPosition = 20;
    }

    // Technical Skills
    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(138, 43, 226);
    doc.text('TECHNICAL SKILLS', margin, yPosition);
    yPosition += 8;

    doc.setFontSize(10);
    doc.setFont('helvetica', 'normal');
    doc.setTextColor(0, 0, 0);

    const skills = [
      { category: 'Frontend', items: 'Angular 19, TypeScript, JavaScript (ES6+), HTML5, CSS3/SCSS, RxJS, NgRx' },
      { category: 'UI Frameworks', items: 'Material Design, PrimeNG, Bootstrap, Tailwind CSS' },
      { category: 'Tools & Technologies', items: 'Git, RESTful APIs, Responsive Design, State Management, Webpack' },
      { category: 'Methodologies', items: 'Agile/Scrum, CI/CD, Test-Driven Development, Code Review' }
    ];

    skills.forEach(skill => {
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(10);
      doc.text(`${skill.category}:`, margin, yPosition);
      yPosition += 5;

      doc.setFont('helvetica', 'normal');
      doc.setFontSize(10);
      const skillLines = doc.splitTextToSize(skill.items, pageWidth - 2 * margin - 10);
      doc.text(skillLines, margin + 10, yPosition);
      yPosition += skillLines.length * 5;
      yPosition += 3;
    });
    yPosition += 4;

    // Key Projects
    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(138, 43, 226);
    doc.text('KEY PROJECTS', margin, yPosition);
    yPosition += 8;

    doc.setFontSize(11);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(0, 0, 0);
    doc.text('Visa2Fly - Online Visa Application Platform', margin, yPosition);
    yPosition += 7;

    doc.setFontSize(9);
    doc.setFont('helvetica', 'normal');
    const project1 = 'Comprehensive online visa application platform with AI-powered document validation, priority processing, support for 50+ countries, real-time tracking, and seamless payment integration. Processed 500,000+ visas with 99.3% approval rate.';
    const project1Lines = doc.splitTextToSize(project1, pageWidth - 2 * margin - 5);
    doc.text(project1Lines, margin, yPosition);
    yPosition += project1Lines.length * 4.5;
    yPosition += 4;

    doc.setFontSize(8);
    doc.setFont('helvetica', 'italic');
    const tech1Lines = doc.splitTextToSize('Technologies: Angular 19, TypeScript, RxJS, SCSS, RESTful APIs, Responsive Design', pageWidth - 2 * margin - 5);
    doc.text(tech1Lines, margin, yPosition);
    yPosition += tech1Lines.length * 4;
    yPosition += 6;

    doc.setFontSize(11);
    doc.setFont('helvetica', 'bold');
    doc.text('White-Label Partner Integrations', margin, yPosition);
    yPosition += 7;

    doc.setFontSize(9);
    doc.setFont('helvetica', 'normal');
    const project2 = 'Successfully integrated Visa2Fly platform with 24+ leading travel and fintech brands including IndiGo, SpiceJet, Vistara, ixigo, EaseMyTrip, and Yatra. Implemented multi-tenant architecture with custom theming and configurations.';
    const project2Lines = doc.splitTextToSize(project2, pageWidth - 2 * margin - 5);
    doc.text(project2Lines, margin, yPosition);
    yPosition += project2Lines.length * 4.5;
    yPosition += 4;

    doc.setFontSize(8);
    doc.setFont('helvetica', 'italic');
    const tech2Lines = doc.splitTextToSize('Technologies: Angular 19, Multi-tenant Architecture, Custom Theming, Dynamic Configuration', pageWidth - 2 * margin - 5);
    doc.text(tech2Lines, margin, yPosition);
    yPosition += tech2Lines.length * 4;
    yPosition += 8;

    // Achievements
    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(138, 43, 226);
    doc.text('KEY ACHIEVEMENTS', margin, yPosition);
    yPosition += 8;

    doc.setFontSize(10);
    doc.setFont('helvetica', 'normal');
    doc.setTextColor(0, 0, 0);

    const achievements = [
      '• Successfully delivered enterprise-scale applications serving 500,000+ users',
      '• Achieved 99.3% visa approval rate through optimized user experience and validation',
      '• Integrated 24+ white-label partner solutions for leading airlines and travel platforms',
      '• Improved application performance by 40% through code optimization',
      '• Led frontend architecture decisions for multi-tenant platform'
    ];

    achievements.forEach(item => {
      doc.setFontSize(10);
      doc.setFont('helvetica', 'normal');
      const lines = doc.splitTextToSize(item, pageWidth - 2 * margin - 5);
      doc.text(lines, margin, yPosition);
      yPosition += lines.length * 5;
    });

    // Footer
    doc.setFontSize(8);
    doc.setFont('helvetica', 'italic');
    doc.setTextColor(100, 100, 100);
    doc.text('Generated from portfolio - jahulkhan.dev', pageWidth / 2, pageHeight - 10, { align: 'center' });

    // Save the PDF
    doc.save('Jahul_Khan_Resume.pdf');
  }
}

