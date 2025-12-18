---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.Modernizer.Cmdlets.dll-Help.xml
Module Name: AppvSequencer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvsequencer/update-appvsequencerpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-AppvSequencerPackage
---

# 更新 AppvSequencerPackage

## 摘要
升级虚拟应用程序包。

## 语法

```
Update-AppvSequencerPackage [-FullLoad] [-InputPackagePath] <String> [-Installer] <String[]>
 [-InstallerOptions <String[]>] [-Name] <String> [-Path] <String> [-TemplateFilePath <String>]
 [<CommonParameters>]
```

## 描述
`Update-AppvSequencerPackage` cmdlet 用于升级虚拟应用程序包。它接受三个输入参数：原始包文件、升级安装程序以及输出路径。执行该 cmdlet 后，会得到一个已升级的包文件作为返回结果。

## 示例

#### 示例 1：更新应用程序
```
PS C:\> Update-AppvSequencerPackage -AppvPackageFilePath "C:\Packages\MyPackage.appv" -Installer "C:\PackageInstall\PackageUpgrade.exe" -OutputPath "C:\UpgradedPackages"
```

这个命令用于更新应用程序，并更改输出路径。

### 示例 2：更新应用程序并要求包被完全加载
```
PS C:\> Update-AppvSequencerPackage -AppvPackageFilePath "C:\Packages\MyPackage.appv" -Installer "C:\PackageInstall\PackageUpgrade.exe" -OutputPath "C:\UpgradedPackages" -FullLoad
```

这个命令用于更新应用程序，并将相关包设置为完全加载状态。

## 参数

### -FullLoad
这表示该 cmdlet 在启动包之前会强制将其完全下载到计算机上。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputPackagePath
指定要升级的现有Microsoft应用程序虚拟化（App-V）包的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Installer
指定用于升级 App-V 包的安装程序。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InstallerOptions
指定一个安装程序命令行选项数组作为参数值，例如 /quiet、/passive 或 /norestart。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定在序列化过程中给出的包的友好名称。该值是从包清单中获取的。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定用于保存更新后的软件包的文件夹路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: OutputPath

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TemplateFilePath
指定用于创建此应用程序包的应用程序虚拟化（App-V）包模板文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Expand-AppvSequencerPackage](./Expand-AppvSequencerPackage.md)

[New-AppvSequencerPackage](./New-AppvSequencerPackage.md)

