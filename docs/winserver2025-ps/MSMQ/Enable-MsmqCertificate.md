---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Msmq.PowerShell.Commands.dll-Help.xml
Module Name: MSMQ
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/msmq/enable-msmqcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-MsmqCertificate
---

# Enable-MsmqCertificate

## 摘要
将证书注册到 Active Directory 域服务中。

## 语法

### InputObject
```
Enable-MsmqCertificate -InputObject <X509Certificate2> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 更新内部证书（RenewInternalCertificate）
```
Enable-MsmqCertificate [-RenewInternalCertificate] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-MsmqCertificate` 这个cmdlet用于将证书注册到Active Directory®域服务中。如果你指定了`RenewInternalCertificate`参数，该cmdlet会在你的个人证书存储中生成一个新的证书，并将其注册到Active Directory域服务中。执行此cmdlet后，会返回一个`System SECURITY.Cryptography.X509Certificates.X509Certificate`对象，该对象表示已成功注册的证书。

## 示例

#### 示例 1：注册证书
```
PS C:\> $_ | Enable-MsmqCertificate
```

此命令用于注册存储在管道对象变量中的证书。请将该命令作为使用该管道的脚本的一部分来使用。有关更多信息，请输入 `Get-Help about_Automatic_variables`。

### 示例 2：创建并注册证书
```
PS C:\> Enable-MsmqCertificate -RenewInternalCertificate
```

此命令会在您的个人证书存储中生成一个证书，并将其注册到 Active Directory 域服务中。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定一个证书对象，该对象代表此cmdlet要注册到Active Directory域服务中的证书。如果您指定了*RenewInternalCertificate*参数，则无法再指定此参数。

```yaml
Type: X509Certificate2
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -RenewInternalCertificate
该参数表示此cmdlet会在用户的个人证书存储中生成一个证书，并将该证书注册到Active Directory域服务中。如果您通过管道运算符将某个证书传递给此cmdlet，则无法指定此参数。

```yaml
Type: SwitchParameter
Parameter Sets: RenewInternalCertificate
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Security Cryptography.X509Certificates.X509Certificate2

## 输出

### System.Object

## 备注

## 相关链接

[Get-MsmqCertificate](./Get-MsmqCertificate.md)

[Remove-MsmqCertificate](./Remove-MsmqCertificate.md)

