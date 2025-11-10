# app

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

lib/
├── main.dart
├── core/
│   ├── constants/
│   ├── utils/
│   └── widgets/        # truly reusable components
├── features/
│   └── auth/
│       └── presentation/
│           ├── screens/
│           ├── widgets/
│           └── controllers/   # state management later
├── screens/            # Other non-feature-specific screens
├── widgets/            # Global widgets
├── theme/
│   ├── app_colors.dart
│   ├── app_text_styles.dart
│   └── app_theme.dart
└── routes/
    └── app_routes.dart

