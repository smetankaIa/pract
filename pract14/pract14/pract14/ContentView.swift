//
//  ContentView.swift
//  pract14
//
//  Created by Алексей Никулин on 25.03.2025.
//

import SwiftUI

struct SplashScreenView: View {
    @State private var showMainView = false

    var body: some View {
        ZStack {
            Image("splash") // Замените "splashImage" на имя вашего изображения в Assets
                .resizable()
                .scaledToFill()
                .edgesIgnoringSafeArea(.all)

            VStack {
                Spacer()
                Button("Перейти") {
                    showMainView = true
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            .padding()
        }
        .fullScreenCover(isPresented: $showMainView) {
            MainView()
        }
    }
}

struct MainView: View {
    @Environment(\.dismiss) var dismiss
    @State private var showingAlert = false

    var body: some View {
        NavigationView {
            Text("Основное окно")
                .navigationTitle("Главная")
                .toolbar {
                    ToolbarItem(placement: .navigationBarTrailing) {
                        Button("Закрыть") {
                            showingAlert = true
                        }
                    }
                }
                .alert(isPresented: $showingAlert) {
                    Alert(
                        title: Text("Подтверждение"),
                        message: Text("Вы уверены, что хотите закрыть окно?"),
                        primaryButton: .destructive(Text("Закрыть"), action: {
                            dismiss()
                        }),
                        secondaryButton: .cancel(Text("Отмена"))
                    )
                }
        }
    }
}



#Preview {
    SplashScreenView()
}
