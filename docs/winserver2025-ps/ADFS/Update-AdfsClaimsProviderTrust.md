---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/update-adfsclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-AdfsClaimsProviderTrust
---

# 更新 AdfsClaimsProviderTrust

## 摘要
根据联邦元数据更新对声明提供者的信任关系。

## 语法

### 标识符Object
```
Update-AdfsClaimsProviderTrust [-MetadataFile <String>] -TargetClaimsProviderTrust <ClaimsProviderTrust>
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TokenSigningCertificates
```
Update-AdfsClaimsProviderTrust [-MetadataFile <String>] -TargetCertificate <X509Certificate2> [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符
```
Update-AdfsClaimsProviderTrust [-MetadataFile <String>] -TargetIdentifier <String> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 标识符Name
```
Update-AdfsClaimsProviderTrust [-MetadataFile <String>] -TargetName <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Update-AdfsClaimsProviderTrust` cmdlet 根据联合元数据更新声明提供者的信任关系设置。

## 示例

## 参数

### -MetadataFile
指定一个UNC文件路径，该文件包含用于声明提供者的联合元数据信息。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetCertificate
指定需要更新的声明提供者信任（claims provider trust）中的令牌签名证书（token-signing certificate）。

```yaml
Type: X509Certificate2
Parameter Sets: TokenSigningCertificates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClaimsProviderTrust
指定要更新的声明提供者信任关系（claim provider trust）。该值通常来自处理流程（pipeline）。

```yaml
Type: ClaimsProviderTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定要更新的声明提供者信任关系的标识符。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要更新的声明提供者信任（claims provider trust）的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Security.Cryptography.X509Certificates.X509Certificate.X509Certificate2

`X509Certificate2` 对象是通过 `*TargetCertificate*` 参数接收到的。

### MicrosoftIdentityServer.PowShell.ResourcesClaimsProviderTrust

`ClaimsProviderTrust` 对象是通过 `*TargetClaimsProviderTrust*` 参数接收到的。

### System.String

字符串对象通过*TargetIdentifier*和*TargetName*参数被接收。

## 输出

### MicrosoftIdentityServer.PowShell.ResourcesClaimsProviderTrust

当指定 *PassThru* 参数时，该命令会返回更新后的 ClaimsProviderTrust 对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-AdfsClaimsProviderTrust](./Add-AdfsClaimsProviderTrust.md)

[禁用 AdfsClaimsProviderTrust](./Disable-AdfsClaimsProviderTrust.md)

[Enable-AdfsClaimsProviderTrust](./Enable-AdfsClaimsProviderTrust.md)

[Get-AdfsClaimsProviderTrust](./Get-AdfsClaimsProviderTrust.md)

[Remove-AdfsClaimsProviderTrust](./Remove-AdfsClaimsProviderTrust.md)

[Set-AdfsClaimsProviderTrust](./Set-AdfsClaimsProviderTrust.md)

