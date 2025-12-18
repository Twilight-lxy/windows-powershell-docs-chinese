---
description: 将一个已签名（加密）的应用程序包添加到用户账户中。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/add-appxpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AppxPackage
---

# 添加 AppxPackage 文件

## 摘要
将一个已签名（加密）的应用程序包添加到用户账户中。

## 语法

### AddSet（默认值）

```
Add-AppxPackage [-Path] <String> [-DependencyPath <String[]>] [-RequiredContentGroupOnly]
 [-ForceApplicationShutdown] [-ForceTargetApplicationShutdown] [-ForceUpdateFromAnyVersion]
 [-RetainFilesOnFailure] [-InstallAllResources] [-Volume <AppxVolume>]
 [-ExternalPackages <String[]>] [-OptionalPackages <String[]>] [-RelatedPackages <String[]>]
 [-ExternalLocation <String>] [-DeferRegistrationWhenPackagesAreInUse]
 [-StubPackageOption <StubPackageOption>] [-AllowUnsigned] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AddByAppInstallerSet

```
Add-AppxPackage [-Path] <String> [-RequiredContentGroupOnly] [-AppInstallerFile]
 [-ForceTargetApplicationShutdown] [-InstallAllResources] [-LimitToExistingPackages]
 [-Volume <AppxVolume>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RegisterSet

```
Add-AppxPackage [-Path] <String> [-DependencyPath <String[]>] [-Register] [-DisableDevelopmentMode]
 [-ForceApplicationShutdown] [-ForceTargetApplicationShutdown] [-ForceUpdateFromAnyVersion]
 [-InstallAllResources] [-ExternalLocation <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UpdateSet

```
Add-AppxPackage [-Path] <String> [-DependencyPath <String[]>] [-RequiredContentGroupOnly]
 [-ForceApplicationShutdown] [-ForceTargetApplicationShutdown] [-ForceUpdateFromAnyVersion]
 [-RetainFilesOnFailure] [-InstallAllResources] [-Update] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### StageSet

```
Add-AppxPackage [-Path] <String> [-DependencyPath <String[]>] [-RequiredContentGroupOnly] [-Stage]
 [-ForceUpdateFromAnyVersion] [-Volume <AppxVolume>] [-ExternalPackages <String[]>]
 [-OptionalPackages <String[]>] [-RelatedPackages <String[]>] [-ExternalLocation <String>]
 [-StubPackageOption <StubPackageOption>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RegisterByPackageFullNameSet

```
Add-AppxPackage [-Register] -MainPackage <String> [-DependencyPackages <String[]>]
 [-ForceApplicationShutdown] [-ForceTargetApplicationShutdown] [-ForceUpdateFromAnyVersion]
 [-InstallAllResources] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RegisterByPackageFamilyNameSet

```
Add-AppxPackage [-RegisterByFamilyName] -MainPackage <String> [-DependencyPackages <String[]>]
 [-ForceApplicationShutdown] [-ForceTargetApplicationShutdown] [-InstallAllResources]
 [-OptionalPackages <String[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Add-AppxPackage` cmdlet 可将已签名的应用包添加到用户账户中。应用包的文件扩展名为 `.msix` 或 `.appx`。可以使用 **DependencyPath** 参数来添加安装该应用包所需的所有其他包。

在开发Windows商店应用程序时，您可以使用`Register`参数从未打包的文件文件夹中安装这些文件。

要更新已安装的软件包，新软件包必须具有相同的软件包系列名称（package family name）。

## 示例

### 示例 1：添加一个应用包

```powershell
Add-AppxPackage -Path '.\MyApp.msix' -DependencyPath '.\winjs.msix'
```

这个命令会添加一个应用程序包及其所包含的内容。

### 示例 2：更新应用程序，但将注册操作推迟到应用程序关闭之后再进行

```powershell
$params = @{
    Path = '.\MyApp.msix'
    DependencyPath = '.\winjs.msix'
    DeferRegistrationWhenPackagesAreInUse = $true
}
Add-AppxPackage @params
```

这条命令会注册对现有应用的更新，但直到应用下次启动时，更新才会真正生效。

#### 示例 3：在开发模式下添加一个被禁用的应用程序包

```powershell
$InstallLocation = Get-AppxPackage -Name '*WindowsCalculator*' |
    Select-Object -ExpandProperty InstallLocation
$ManifestPath = $InstallLocation + '\Appxmanifest.xml'
Add-AppxPackage -Path $ManifestPath -Register -DisableDevelopmentMode
```

该命令用于获取已安装的 Windows Store 应用程序的包清单文件（package manifest file）的完整路径，然后注册该包。你可以使用 **DisableDevelopmentMode** 来注册那些通过 **StagePackageAsync** API 进行处理的、已被禁用的，或在测试过程中损坏的应用程序。

### 示例 4：添加一个应用程序及其可选的包

```powershell
Add-AppxPackage -Path '.\MyApp.msixbundle' -ExternalPackages @(
    '.\optionalpackage1.msix'
    '.\optionalpackage2.msixbundle'
)

Add-AppxPackage -Path '.\MyApp.msixbundle' -OptionalPackages '29270sandstorm.OptionalPackage1_gah1vdar1nn7a'
```

此命令会添加一个应用程序包及其可选的附加包。这是一个原子操作（即整个过程是不可分割的），这意味着如果应用程序或其可选包的安装失败，那么部署操作将会被终止。

### 示例 5：仅安装流媒体应用程序中所需的部分

```powershell
Add-AppxPackage -Path '.\MyApp.msixbundle' -RequiredContentGroupOnly
```

此命令用于添加一个应用程序包，但仅安装流媒体应用程序中所需的组件。如果再次调用该命令时不使用 `RequiredContentGroupOnly` 参数，则会按照 `AppxContentGroupMap.xml` 中定义的顺序安装应用程序的其余部分。

### 示例 6：使用应用安装程序文件来安装应用程序

```powershell
Add-AppxPackage -AppInstallerFile "C:\Users\user1\Desktop\MyApp.appinstaller"
```

此命令会根据“App Installer”文件中的说明添加一个应用程序包，并应用该文件中指定的所有更新设置（如果有的话）。

## 参数

### -AllowUnsigned

允许添加一个未签名的软件包。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AppInstallerFile

运行一个应用程序安装程序文件，让用户只需点击一下即可安装所有已定义的软件包。有关更多信息，请参阅[手动创建应用程序安装程序文件](/windows/msix/app-installer/how-to-create-app installer-file)。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddByAppInstallerSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DeferRegistrationWhenPackagesAreInUse

该设置表明：如果应用程序当前正在使用中，则不会为用户进行注册操作。下次启动应用程序时，系统会自动更新相关配置。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -DependencyPackages

指定要注册的依赖包的全名或依赖包捆绑包的全名。

```yaml
Type: System.String[]
Parameter Sets: RegisterByPackageFullNameSet, RegisterByPackageFamilyNameSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -DependencyPath

指定一个包含依赖包文件路径的数组，这些依赖包是安装应用程序包所必需的。应用程序包的文件扩展名为 `.msix`、`.appx`、`.msixbundle` 或 `.appxbundle`。您可以指定多个依赖包的路径。如果某个依赖包已经安装在用户设备上，则可以不需要将其添加到 `DependencyPath` 中。

```yaml
Type: System.String[]
Parameter Sets: AddSet, RegisterSet, UpdateSet, StageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableDevelopmentMode

该参数表示此 cmdlet 用于注册一个已禁用的、未成功注册的或已损坏的应用程序包安装。使用该参数可指定应用程序清单文件来自现有的安装实例，而非处于开发模式下的文件集合。您还可以利用该参数来注册通过 [包管理器 API](https://go.microsoft.com/fwlink/?LinkId=245447) 提供的应用程序。请使用 **Register** 参数指定应用程序包清单文件（`.xml` 格式）在安装路径中的位置。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RegisterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExternalLocation

MSIX包之外的外部磁盘位置的URI路径；该位置用于存储应用程序内容，且包清单（package manifest）可以引用这些内容。

```yaml
Type: System.String
Parameter Sets: AddSet, RegisterSet, StageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExternalPackages

指定了一组可选的包，这些包必须与应用程序包一起安装。这是一个原子操作（即不可分割的操作）：如果应用程序或其可选包的安装失败，那么部署操作将会被终止。

```yaml
Type: System.String[]
Parameter Sets: AddSet, StageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceApplicationShutdown

该参数表示此 cmdlet 会强制关闭与包或其依赖项关联的所有正在运行的进程。如果您指定了此参数，请不要同时指定 **ForceTargetApplication Shutdown** 参数。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet, RegisterSet, UpdateSet, RegisterByPackageFullNameSet, RegisterByPackageFamilyNameSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceTargetApplicationShutdown

表示此cmdlet会强制与该软件包关联的所有正在运行的进程关闭。如果您指定了此参数，则不要同时指定**ForceApplicationShutdown**参数。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet, AddByAppInstallerSet, RegisterSet, UpdateSet, RegisterByPackageFullNameSet, RegisterByPackageFamilyNameSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceUpdateFromAnyVersion

这个参数用于强制将某个包的特定版本进行暂存或注册，无论是否已经有更高版本的该包被暂存或注册过。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet, RegisterSet, UpdateSet, StageSet, RegisterByPackageFullNameSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstallAllResources

表示该 cmdlet 强制部署从包参数中指定的所有资源包。这会覆盖部署引擎对资源适用性的检查，强制执行所有资源包的暂存（staging）操作、注册操作，或同时执行这两项操作。此参数只能在指定资源包或资源包清单时使用。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet, AddByAppInstallerSet, RegisterSet, UpdateSet, RegisterByPackageFullNameSet, RegisterByPackageFamilyNameSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LimitToExistingPackages

这个参数用于防止遗漏需要下载的引用包。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddByAppInstallerSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MainPackage

指定要注册的主要包的全名或捆绑包的全名。

```yaml
Type: System.String
Parameter Sets: RegisterByPackageFullNameSet, RegisterByPackageFamilyNameSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -OptionalPackages

指定与应用程序一起需要安装的相关可选包的 `PackageFamilyName`。与 `externalPackages` 标志不同，您无需提供这些可选包的路径。这是一个原子操作（即整个过程是不可分割的）：如果应用程序或其可选包无法安装，则部署操作将会被终止。

```yaml
Type: System.String[]
Parameter Sets: AddSet, StageSet, RegisterByPackageFamilyNameSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定应用程序包文件的路径。应用程序包的文件扩展名可以是`.msix`、`.appx`、`.msixbundle`或`.appxbundle`。

```yaml
Type: System.String
Parameter Sets: AddSet, AddByAppInstallerSet, RegisterSet, UpdateSet, StageSet
Aliases: PSPath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Register

该 cmdlet 表示以开发模式注册一个应用程序。您可以使用开发模式从未压缩的文件文件夹中安装应用程序；在将应用程序部署为应用包之前，也可以通过这种方式对其进行测试。要注册已存在的应用程序包，请必须同时指定 `DisableDevelopmentMode` 参数和 `Register` 参数。如果要指定依赖包，则需要使用 `DependencyPath` 参数以及 `DisableDevelopmentMode` 参数。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RegisterSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RegisterByPackageFullNameSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RegisterByFamilyName

指定参数 `-MainPackage`，该参数用于定义要注册的家族名称或全名。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: RegisterByPackageFamilyNameSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RelatedPackages

这是一个可选元素，用于指定在主应用程序包中指定的其他可选软件包。这些软件包不会作为部署操作的一部分被安装。

```yaml
Type: System.String[]
Parameter Sets: AddSet, StageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequiredContentGroupOnly

该设置表示只需安装《AppxContentGroupMap.xml》中指定的所需内容组即可。完成这些步骤后，应用程序就可以启动了。调用`Add-AppxPackage`命令并指定应用程序的路径时，系统会按照《AppxContentGroupMap.xml》中定义的顺序安装应用程序的其余部分。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet, AddByAppInstallerSet, UpdateSet, StageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RetainFilesOnFailure

在部署失败的情况下，如果将此开关设置为 `$true`，则在安装过程中在目标机器上创建的文件将不会被删除。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AddSet, UpdateSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Stage

将一个软件包部署到系统中，但不对其进行注册。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: StageSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StubPackageOption

定义了正在被添加或暂存的应用包的“stub”（占位）行为。该参数的可接受值为：

- `Default`: Uses the default behavior
- `InstallFull`: Installs as a full app
- `InstallStub`: Installs as a stub app
- `UsePreference`: Uses the current
  [PackageStubPreference](/uwp/api/windows.management.deployment.packagestubpreference) for the
  package

```yaml
Type: StubPackageOption
Parameter Sets: AddSet, StageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Update

该参数表示要添加的包是一个依赖包更新。当父应用程序被删除时，相应的依赖包也会从用户账户中移除。如果不使用此参数，则所添加的包将作为主包处理；即使父应用程序被删除，该主包也不会从用户账户中移除。如果要更新已安装的包，新包必须具有与旧包相同的包家族名称。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: UpdateSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Volume

指定用于放置该包的 **AppxVolume** 对象。此卷同时也指定了用户 **AppData** 的默认存储位置。

```yaml
Type: AppxVolume
Parameter Sets: AddSet, AddByAppInstallerSet, StageSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm

在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### System.IO.FileInfo

## 输出

### 无

## 备注

## 相关链接

[包管理器 API](https://go.microsoft.com/fwlink/?LinkId=245447)

[如何添加和删除应用程序](https://go.microsoft.com/fwlink/?LinkID=231020)

[Get-AppxPackage](./Get-AppxPackage.md)

[Get-AppxPackageManifest](./Get-AppxPackageManifest.md)

[Move-AppxPackage](./Move-AppxPackage.md)

[Remove-AppxPackage](./Remove-AppxPackage.md)
