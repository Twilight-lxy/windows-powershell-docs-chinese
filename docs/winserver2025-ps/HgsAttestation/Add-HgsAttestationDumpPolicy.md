---
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
online version: https://learn.microsoft.com/powershell/module/hgsattestation/add-hgsattestationdumppolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-HgsAttestationDumpPolicy
---

# Add-HgsAttestationDumpPolicy

## 摘要
将一个授权的转储加密密钥添加到HGS中。

## 语法

### 控制台（默认设置）
```
Add-HgsAttestationDumpPolicy [-PublicKeyHash] <String> -Name <String> [-PolicyVersion <PolicyVersion>] [-Stage]
 [-WhatIf] [-Confirm]
```

### 文件
```
Add-HgsAttestationDumpPolicy [-Path] <String> [-Name <String>] [-PolicyVersion <PolicyVersion>] [-Stage]
 [-WhatIf] [-Confirm]
```

## 描述
`Add-HgsAttestationDumpPolicy` cmdlet 允许使用指定的密钥来加密 Hyper-V 主机上的内存转储文件。只有那些使用授权密钥进行加密的主机，以及那些不允许任何内存转储操作的主机，才能成功完成验证（attest）过程。

## 示例

### 示例 1
```
PS C:\> Add-HgsAttestationDumpPolicy -PublicKeyHash 'e91c254ad58860a02c788dfb5c1a65d6a8846ab1dc649631c7db16fef4af2dec' -Name 'Contoso Dump Encryption'
```

将转储加密密钥以及指定的SHA256公钥哈希值添加到HGS中。

### 示例 2
```
PS C:\> Add-HgsAttestationDumpPolicy -Path 'C:\temp\TpmBaselineWithDumpEncryption.tcglog' -Name 'Contoso Dump Encryption'
```

在主机配置为使用转储加密功能后，通过TCG日志（TPM基线）将转储加密密钥添加到HGS中。

## 参数

### -Name
用于描述转储策略的友好名称（即易于理解的名称）。

```yaml
Type: String
Parameter Sets: Console
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: File
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定一个 TPM 基线文件（TCG 日志）的路径，该文件包含转储加密证书的公钥哈希值。在配置好 Hyper-V 主机以使用转储加密功能后，应获取相应的 TPM 基线文件。

```yaml
Type: String
Parameter Sets: File
Aliases: FilePath, PSPath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PolicyVersion
保留以供将来使用。

```yaml
Type: PolicyVersion
Parameter Sets: (All)
Aliases:
Accepted values: None, PolicyVersion1503, PolicyVersion1704

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PublicKeyHash
用于转储加密的证书的公钥的 SHA256 哈希值。

```yaml
Type: String
Parameter Sets: Console
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Stage
保留以供将来使用。

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

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

## 输入

### System.String


## 输出

### System.Object

## 备注

## 相关链接

