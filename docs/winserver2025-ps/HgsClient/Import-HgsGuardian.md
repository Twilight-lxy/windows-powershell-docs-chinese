---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/import-hgsguardian?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-HgsGuardian
---

# 导入 HgsGuardian

## 摘要
从.xml文件中创建一个guardian对象。

## 语法

```
Import-HgsGuardian [-Path] <String> -Name <String> [-AllowExpired] [-AllowUntrustedRoot] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Import-HgsGuardian` 这个cmdlet可以从一个.xml文件中创建一个Host Guardian Service守护对象。如果你为该守护对象指定了一个名称，这个cmdlet还会将该对象保存到本地的守护对象存储中。

## 示例

### 示例 1：导入一个守护者（Guardian）
```
PS C:\> Import-HgsGuardian -Path "C:\MyDirectory\Guardian11.xml" -Name "Guardian11"
```

这个命令从指定的.xml文件中导入一个守护程序（guardian）。

## 参数

### -AllowExpired
表示是否允许使用已过期的证书来创建守护者（guardian）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowUntrustedRoot
指示是否允许使用自签名证书来创建守护者（guardian）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定在将该守护者信息保存到本地守护者存储时所使用的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定包含《卫报》相关信息的XML文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FilePath

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
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
Default value: None
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### CimInstance#MSFT_HgsGuardian
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Export-HgsGuardian](./Export-HgsGuardian.md)

[Get-HgsGuardian](./Get-HgsGuardian.md)

[New-HgsGuardian](./New-HgsGuardian.md)

[Remove-HgsGuardian](./Remove-HgsGuardian.md)

