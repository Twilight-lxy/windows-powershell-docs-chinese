---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/export-hgsserverstate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-HgsServerState
---

# Export-HgsServerState

## 摘要
将本地Host Guardian服务实例的状态导出，以便在需要恢复的情况下使用。

## 语法

```
Export-HgsServerState [[-Path] <String>] -Password <SecureString> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Export-HgsServer` cmdlet 可以导出 Host Guardian Service (HGS) 的状态信息，以便用于恢复相关场景。

此 cmdlet 会导致以下 Host Guardian Service 状态被导出到指定的输出文件中：

- Attestation Service policies
- Attestation Service configuration data
- Key Protection policies
- Key Protection configuration data
- Key Protection Signer Certificates and private keys
- Key Protection Encryption Certificates and private keys

有关场景术语的更多信息，请参阅[安全与保障](https://go.microsoft.com/fwlink/?LinkId=699209)。

## 示例

### 示例 1：导出 HGS 服务器的状态，并用密码进行保护
```
PS C:\> Export-HgsServerState -Path "C:\HGS\ExportState.xml" -Password $Pass
Encrypted HGS Server State stored at the specified location
```

该命令用于导出HGS服务器的状态，并使用密码对导出的状态进行保护。导出的状态将被存储在由**Path**参数指定的文件中。

使用 `ConvertTo-SecureString` cmdlet 生成一个表示密码的安全字符串。

## 参数

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

### -Password
指定用于加密密钥的密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定导出文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FilePath

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[HGS 服务器 cmdlet](./hgsserver.md)

