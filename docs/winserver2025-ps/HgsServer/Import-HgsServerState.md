---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/import-hgsserverstate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-HgsServerState
---

# 导入 HgsServerState 类

## 摘要
将导出的Host Guardian Service状态导入到一个Host Guardian Service实例中。

## 语法

### XML
```
Import-HgsServerState [[-XML] <XmlDocument>] -Password <SecureString> [-ImportTpmModeState]
 [-ImportActiveDirectoryModeState] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 文件
```
Import-HgsServerState [[-Path] <String>] -Password <SecureString> [-ImportTpmModeState]
 [-ImportActiveDirectoryModeState] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-HgsServer` cmdlet 将之前导出的 Host Guardian Service（HGS）状态数据导入到现有的 Host Guardian Service 实例中。

该cmdlet从输入文件中导入以下Host Guardian服务的状态信息：

- Attestation service policies
- Attestation service configuration data
- Key protection policies
- Key protection configuration data
- Key Protection Signer Certificates and private keys
- Key Protection Encryption Certificates and private keys

此外，此cmdlet还会更新证书签名服务（attestation service）的证书，并使用该证书来更新密钥保护服务实例（key protection service）。

有关场景术语的更多信息，请参阅[安全与保障](https://go.microsoft.com/fwlink/?LinkId=699209)。

## 示例

#### 示例 1：导入 HGS 状态数据
```
PS C:\> Import-HgsServerState -Path "C:\ExportedHgsServerState.xml" -Password $Pass
```

此命令用于将之前导出的状态数据导入到当前的HGS（Highly Granular Server）服务器中。该命令只能在一个节点上执行，导入的状态数据会自动复制到HGS服务器设置中的其他节点上。

导出的状态数据是执行 `Export-HgsServerState` 命令时针对现有 HGS 服务器设置所生成的输出结果。指定的密码必须与传递给 `Export-HgsServerState` 的密码相匹配。

使用 `ConvertTo-SecureString` 函数生成一个表示密码的安全字符串。

## 参数

### -ImportActiveDirectoryModeState
表示此cmdlet会导入并更新与Active Directory操作模式相关的认证服务配置状态。

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

### -ImportTpmModeState
表示此cmdlet会导入并更新与受信任平台模块（TPM）操作模式相关的认证服务配置状态。

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
指定 `Export-HgsServerState` cmdlet 用于加密密钥时使用的密码。

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
指定此 cmdlet 导入的文件的路径。

```yaml
Type: String
Parameter Sets: File
Aliases: FilePath

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -XML
指定此cmdlet作为XML文档导入的状态。

```yaml
Type: XmlDocument
Parameter Sets: XML
Aliases: InputObject

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

## 备注

## 相关链接

[Export-HgsServerState](./Export-HgsServerState.md)

[HGS 服务器 cmdlet](./hgsserver.md)

