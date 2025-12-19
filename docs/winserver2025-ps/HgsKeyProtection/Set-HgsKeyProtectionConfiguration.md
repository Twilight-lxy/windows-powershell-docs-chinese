---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.KpsServer.Administration.dll-Help.xml
Module Name: HgsKeyProtection
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgskeyprotection/set-hgskeyprotectionconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-HgsKeyProtectionConfiguration
---

# 设置 HgsKeyProtectionConfiguration

## 摘要
修改密钥保护服务的配置。

## 语法

### CertificateReference（默认值）
```
Set-HgsKeyProtectionConfiguration -CommunicationsCertificateThumbprint <String>
 [-NoCommunicationsCertificateReplication] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### FullCertificate
```
Set-HgsKeyProtectionConfiguration -CommunicationsCertificatePath <String>
 [-CommunicationsCertificatePassword <SecureString>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-HgsKeyProtectionConfiguration` cmdlet 为运行在本地计算机上的 Key Protection Service 分配一个通信证书。Key Protection Service 使用该通信证书来签署其提供的元数据文档。

## 示例

### 示例 1：分配一个证书作为通信证书
```
PS C:\> Set-HgsKeyProtectionConfiguration -CommunicationsCertificateThumbprint "d39203a3b3544743ad552afe0615dc1f" -Force
```

此命令将具有指定指纹的证书设置为密钥保护服务（Key Protection Service）的通信证书。该命令包含了“强制执行”（Force）选项，因此不会提示您进行确认。

### 示例 2：将一个证书文件设置为通信证书
```
PS C:\> Set-HgsKeyProtectionConfiguration -CommunicationsCertificatePath "C:\example.pfx"
Set-HgsKeyProtectionConfiguration -CommunicationsCertificateThumbprint "d39203a3b3544743ad552afe0615dc1f" -Force
```

此命令将一个证书文件设置为密钥保护服务（Key Protection Service）的通信证书。

### 示例 3：将包含密码的证书文件设置为通信证书
```
PS C:\> Set-HgsKeyProtectionConfiguration -CommunicationsCertificatePath "C:\example.pfx" -CommunicationsCertificatePassword $Password
```

该命令将一个受密码保护的证书文件设置为密钥保护服务（Key Protection Service）的通信证书。证书的密码以 SecureString 的形式存储在 `$Password` 变量中。

## 参数

### -CommunicationsCertificatePassword
指定用于保护证书文件的密码。如果证书文件需要通过密码进行保护，则必须提供该密码。

```yaml
Type: SecureString
Parameter Sets: FullCertificate
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CommunicationsCertificatePath
指定证书的路径，该证书将被添加到密钥保护服务中作为通信证书使用。

```yaml
Type: String
Parameter Sets: FullCertificate
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CommunicationsCertificateThumbprint
指定新通信证书的“指纹”（即证书的唯一标识）。在运行此 cmdlet 之前，该参数所指定的证书必须已经存在于 LocalMachine\MyCertificates 存储位置中。

```yaml
Type: String
Parameter Sets: CertificateReference
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

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

### -NoCommunicationsCertificateReplication
```yaml
Type: SwitchParameter
Parameter Sets: CertificateReference
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
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
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无
您不能将输入数据通过管道（pipe）传递给这个cmdlet。

## 输出

### 无
此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Get-HgsKeyProtectionConfiguration](./Get-HgsKeyProtectionConfiguration.md)

