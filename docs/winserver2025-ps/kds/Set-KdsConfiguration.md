---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.KeyDistributionService.Cmdlets.dll-Help.xml
Module Name: KDS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/kds/set-kdsconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-KdsConfiguration
---

# Set-KdsConfiguration

## 摘要
设置 Microsoft Group KdsSvc 的配置信息。

## 语法

### KdsConfiguration
```
Set-KdsConfiguration [-LocalTestOnly] [-SecretAgreementPublicKeyLength <Int32>]
 [-SecretAgreementPrivateKeyLength <Int32>] [-SecretAgreementParameters <Byte[]>]
 [-SecretAgreementAlgorithm <String>] [-KdfParameters <Byte[]>] [-KdfAlgorithm <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 恢复到默认设置
```
Set-KdsConfiguration [-LocalTestOnly] [-RevertToDefault] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Set-KdsConfiguration [-LocalTestOnly] [-InputObject] <KdsServerConfiguration> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-KdsConfiguration` cmdlet 用于设置 Microsoft 组密钥分发服务（KdsSvc）的配置。该 cmdlet 设置以下配置数据：

- The key derivation function algorithm and parameters used to generate private group keys
- The secret agreement algorithm and parameters used to generate public group keys

此cmdlet还会通过执行密钥推导函数测试和秘密协商测试来验证输入数据的合法性。

## 示例

### 示例 1：设置 Microsoft 组密钥分发服务（Group Key Distribution Service, GKDSS）的配置
```
PS C:\> $config = Get-KdsConfiguration
PS C:\> Set-KdsConfiguration -InputObject $config
```

此命令使用 **Get-KdsConfiguration** cmdlet 将服务器配置对象检索到一个名为 `$config` 的变量中，并将该变量的内容传递给该 cmdlet。

### 示例 2：在本地服务器上测试配置
```
PS C:\> Set-KdsConfiguration -LocalTestOnly
```

该命令用于测试本地服务器的配置。

### 示例 3：设置密钥派生函数算法
```
PS C:\> Set-KdsConfiguration -KdfAlgorithm "SHA-1"
```

这个命令将密钥派生函数（Key Derivation Function，简称KDF）的算法名称设置为SHA-1。该算法用于生成一个私有的群组密钥。

### 示例 4：设置保密协议算法
```
PS C:\> Set-KdsConfiguration -SecretAgreementAlgorithm "ECDH"
```

这个命令将秘密协议算法的名称设置为 ECDH。该算法用于生成一个公钥群组密钥。

### 示例 5：将组密钥分发服务（Group Key Distribution Service）的配置设置为默认值
```
PS C:\> Set-KdsConfiguration -RevertToDefault
```

该命令用于验证自定义的组密钥分发服务配置是否已被删除，并确保SID密钥开始使用默认配置。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -InputObject
指定用于存储 Microsoft Group KdsSvc 配置信息的服务器配置对象。

```yaml
Type: KdsServerConfiguration
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -KdfAlgorithm
指定密钥分发服务器用于生成密钥的密钥推导函数算法的名称。

```yaml
Type: String
Parameter Sets: KdsConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -KdfParameters
指定用于生成组私钥的密钥推导函数的参数。如果未指定此参数，或者将此参数设置为 $Null，则无需任何密钥推导函数参数。

```yaml
Type: Byte[]
Parameter Sets: KdsConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LocalTestOnly
表示该cmdlet仅验证本地计算机上的新组密钥分发服务配置，并不会将密钥存储在Active Directory中。

如果指定了这个参数，那么该cmdlet会返回一个值，表示测试是否通过。

如果未指定此参数，则该cmdlet会返回新的服务器配置对象。

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

### -RevertToDefault
表示自定义的服务配置已恢复为默认配置。

```yaml
Type: SwitchParameter
Parameter Sets: RevertToDefault
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SecretAgreementAlgorithm
指定用于生成群组公钥的密钥协商算法的名称。

```yaml
Type: String
Parameter Sets: KdsConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecretAgreementParameters
指定秘密协议算法所需的参数。如果未指定该参数，或者将其设置为 `$Null`，则无需任何秘密协议算法参数。

```yaml
Type: Byte[]
Parameter Sets: KdsConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecretAgreementPrivateKeyLength
指定用于秘密协议算法中的私钥的长度。

```yaml
Type: Int32
Parameter Sets: KdsConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SecretAgreementPublicKeyLength
指定用于秘密协议算法中的公钥的长度。

```yaml
Type: Int32
Parameter Sets: KdsConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.KeyDistributionService.KdsServerConfiguration
这个cmdlet返回一个**KdsServerConfiguration**对象，其中包含Microsoft Group KdsSvc的配置信息。

## 输出

### Microsoft.KeyDistributionService.KdsServerConfiguration

### System.Boolean

## 备注

## 相关链接

[Add-KdsRootKey](./Add-KdsRootKey.md)

[Clear-KdsCache](./Clear-KdsCache.md)

[Get-KdsConfiguration](./Get-KdsConfiguration.md)

[Get-KdsRootKey](./Get-KdsRootKey.md)

[测试 KDS 根密钥](./Test-KdsRootKey.md)

