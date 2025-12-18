---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/initialize-rmscryptomode2?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Initialize-RmsCryptoMode2
---

# 初始化 RmsCryptoMode2

## 摘要
为AD RMS服务器过渡到加密模式2做好准备。

## 语法

```
Initialize-RmsCryptoMode2 -FilePath <String[]> [-CspName <String>] [-Regenerate] [-Force] [-Path] <String[]>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Initialize-RmsCryptoMode2` cmdlet 用于准备 Active Directory 权限管理服务（AD RMS）服务器，以便将其切换到加密模式 2。

加密模式2（Cryptographic Mode 2）是经过更新和优化的AD RMS加密实现方案。它支持使用SHA-2哈希算法（SHA-2/SHA-256）标准的2048位RSA加密以及长度为256位的密钥。

虽然这个cmdlet对于完成将AD RMS部署切换到加密模式2所需的初始步骤非常有用，但还需要进行其他操作。首先，AD RMS集群环境中的所有客户端计算机都必须安装相应的补丁以支持这种更新后的增强模式。根据您的部署配置，您可能需要更新部分或全部服务器。当所有计算机的更新工作完成后，作为最终过渡到加密模式2的步骤，您可以运行**Update-ADRMS** cmdlet，并指定*UpdateCryptographicModeOnly*参数，从而有效地将集群从模式1切换到模式2。

## 示例

#### 示例 1：导出 SLC 文件
```
PS C:\> Initialize-RmsCryptoMode2 -Path "." -FilePath "c:\test.tud"
```

该命令将当前 AD RMS 服务器的服务器许可证书（SLC）导出到受信任的用户域 c:\test.tud，适用于使用集中管理密钥的服务器。

### 示例 2：强制重新生成加密模式 2 的密钥
```
PS C:\> Initialize-RmsCryptoMode2 -Path "." -FilePath "c:\test2.tud" -Regenerate

Initialize cryptographic mode 2

This will regenerate the cryptographic mode 2 key pair.  Are you sure you want to continue?

[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):
```

此命令强制重新生成加密模式2所需的密钥。

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

### -CspName
指定在执行此 cmdlet 时用于生成模式 2 TUD 的加密服务提供商（CSP）的名称。该 CSP 必须是 PROVRSA_AES 类型，以支持模式 2 操作（与使用 PROV_RSA_FULL 类型的模式 1 密钥不同）。

*CspName* 参数仅用于基于内容安全策略（CSP）的安装场景。如果为一台使用集中管理密钥的服务器指定了某个 CSP 名称，且该参数被包含在命令中，将会返回错误信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -FilePath
指定当执行此 cmdlet 时生成的文件的名称和位置。该文件包含模式 2 的 SLC（服务器许可证书），在将受信任的用户域（TUD）转换为模式操作的过程中，该证书会被导出。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Force
如果在与 *FilePath* 参数指定的名称和位置下存在同名文件，则该 cmdlet 会强制保存（覆盖）该现有文件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
此参数仅适用于基于内容安全策略（CSP）的安装方式。如果为使用集中管理密钥的服务器指定了CSP名称，而在命令中包含了该参数，则会返回错误信息。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Regenerate
即使之前已经运行过该cmdlet，此命令也会强制AD RMS服务器生成一个新的密钥，并会覆盖任何先前生成的密钥。由于可以多次运行这个cmdlet，如果省略了这个参数，那么每次运行该cmdlet时都会导出相同的密钥。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### string[]、string、bool、SwitchParameter

## 输出

### 无

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

