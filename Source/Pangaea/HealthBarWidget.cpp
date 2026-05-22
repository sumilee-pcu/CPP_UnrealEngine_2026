#include "HealthBarWidget.h"
#include "Blueprint/WidgetTree.h"

void UHealthBarWidget::NativeConstruct()
{
	Super::NativeConstruct();

	if (HealthProgressBar == nullptr && WidgetTree != nullptr)
	{
		HealthProgressBar = WidgetTree->ConstructWidget<UProgressBar>(
			UProgressBar::StaticClass(),
			TEXT("HealthProgressBar")
		);
		WidgetTree->RootWidget = HealthProgressBar;
	}

	SetHealthPercent(1.0f);
}

void UHealthBarWidget::SetHealthPercent(float Percent)
{
	if (HealthProgressBar != nullptr)
	{
		HealthProgressBar->SetPercent(FMath::Clamp(Percent, 0.0f, 1.0f));
	}
}
