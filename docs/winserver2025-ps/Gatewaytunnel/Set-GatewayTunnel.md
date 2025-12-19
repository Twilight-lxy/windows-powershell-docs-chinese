---
external help file: GatewaytunnelConfig_v1.0.cdxml-help.xml
Module Name: Gatewaytunnel
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/gatewaytunnel/set-gatewaytunnel?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-GatewayTunnel
---

# Set-GatewayTunnel

## 摘要
{{ 填写剧情简介 }}

## 语法

```
Set-GatewayTunnel [-TunnelName] <String> [[-RoutingDomainName] <String>] [[-LocalIp] <String>]
 [[-RemoteIp] <String>] [[-TunnelIdentity] <String>] [[-Routes] <String>] [[-LocalExemptRoutes] <String>]
 [[-RemoteExemptRoutes] <String>] [-LocalSubnets <String>] [-Standby <Boolean>] [-AdminStatus <Boolean>]
 [-AutoConnectEnabled <Boolean>] [-ProtocolType <ProtocolType>] [-EncryptionType <EncryptionType>]
 [-IpsecEncryption <IpsecEncryption>] [-IpsecIntegrity <IpsecIntegrity>] [-Pfsgroup <Pfsgroup>]
 [-IkeEncryption <IkeEncryption>] [-IkeIntegrity <IkeIntegrity>] [-Dhgroup <Dhgroup>]
 [-MMSALifeTimeInSeconds <UInt32>] [-SALifeTimeInSeconds <UInt32>] [-SALifeKilloBytes <UInt32>]
 [[-SharedSecret] <String>] [-DpdTimeout <UInt32>] [-UseNarrowTrafficSelectors <Boolean>]
 [-IsConnectionNATed <Boolean>] [-ConnectReason <ConnectReason>] [-TunnelId <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
{{ 填写描述内容 }}

## 示例

### 示例 1
```powershell
PS C:\> {{ Add example code here }}
```

{{ 在这里添加示例描述 }}

## 参数

### -AdminStatus
{{ 填写管理员状态描述 }}

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
{{ 填写工作描述内容 }}

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

### -AutoConnectEnabled
{{ Fill AutoConnectEnabled Description }}

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CimSession
{{ 填写 CimSession 的描述内容 }}

```yaml
Type: Microsoft.Management.Infrastructure.CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ConnectReason
{{ 填写连接原因的描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.ConnectReason
Parameter Sets: (All)
Aliases:
Accepted values: Unknown, ServiceTriggered, DataTriggered, UserTriggered, RemoteTriggered, RemoteCrashTriggered

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Dhgroup
{{ 填写 Dhgroup 描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.Dhgroup
Parameter Sets: (All)
Aliases:
Accepted values: None, DhGroup1, DhGroup2, DhGroup14

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DpdTimeout
{{ 填写 DPDTimeout 的描述 }}

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: Dpd

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EncryptionType
{{ 填写加密类型并描述该加密类型的用途 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.EncryptionType
Parameter Sets: (All)
Aliases:
Accepted values: NoEncryption, StrongEncryption, RequiredEncryption, OptionalEncryption, CustomEncryption

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IkeEncryption
{{ 填写 Ike 加密描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.IkeEncryption
Parameter Sets: (All)
Aliases:
Accepted values: DES, DES3, AES128, AES192, AES256

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IkeIntegrity
{{ 填写关于IkeIntegrity完整性的描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.IkeIntegrity
Parameter Sets: (All)
Aliases:
Accepted values: MD5, SHA1, SHA256, SHA384

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IpsecEncryption
{{ 填写 IPsec 加密说明 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.IpsecEncryption
Parameter Sets: (All)
Aliases: Encryption
Accepted values: DES, DES3, AES128, AES192, AES256, GCMAES128, GCMAES192, GCMAES256, None

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IpsecIntegrity
{{ 填写 IPsec 整合性描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.IpsecIntegrity
Parameter Sets: (All)
Aliases: Auth
Accepted values: MD5, SHA1, SHA256, GCMAES128, GCMAES192, GCMAES256

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IsConnectionNATed
{{ 填写有关 ConnectionNAT 的描述 }}

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LocalExemptRoutes
{{ 填写LocalExemptRoutes的描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 8
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LocalIp
{{ 填写本地IP地址的描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: local

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LocalSubnets
{{ 填写本地子网的描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: LocalSubnet

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MMSALifeTimeInSeconds
{{ 填写 MMSALifeTimeInSeconds 的描述 }}

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: MMSALifeTime

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Pfsgroup
{{ 填写 Pfsgroup 描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.Pfsgroup
Parameter Sets: (All)
Aliases: Pfs
Accepted values: None, PFS1, PFS2, PFS2048, ECP256, ECP384, MM, PFS24

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ProtocolType
{{ 填写协议类型描述 }}

```yaml
Type: Microsoft.PowerShell.Cmdletization.GeneratedTypes.PS_GatewayTunnel.ProtocolType
Parameter Sets: (All)
Aliases:
Accepted values: Ikev2, None

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RemoteExemptRoutes
{{ 填写 RemoteExemptRoutes 的描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 9
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RemoteIp
{{ 填写RemoteIp描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: remote

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Routes
{{ 填充路线描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Route

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RoutingDomainName
{{ 填写 RoutingDomainName 的描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: customer

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SALifeKilloBytes
请帮我填写 {{ Fill SALIFEKilloBytes Description }}

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: SALifeKb

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SALifeTimeInSeconds
{{ 填写 SALIFETimeInSeconds 的描述 }}

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases: SALifeTime

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SharedSecret
{{ 填写 SharedSecret 的描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Presharedkey

Required: False
Position: 7
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Standby
{{ 填充备用说明内容 }}

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
{{ 填写 ThrottleLimit 的描述内容 }}

```yaml
Type: System.Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TunnelId
{{ 填充隧道ID及描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: MMProviderContextKey

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TunnelIdentity
{{ 填写隧道身份描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TunnelName
{{ 填写隧道名称及描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Name

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UseNarrowTrafficSelectors
{{ Fill UseNarrowTrafficselectors Description }}

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System(Boolean)

### Microsoft.PowerShell Cmdletization GeneratedTypes.PS_GatewayTunnel.ProtocolType

### Microsoft.PowShell Cmdletization GeneratedTypes.PS_GatewayTunnel.EncryptionType

### Microsoft.PowerShellCmdletizationGeneratedTypes.PS_GatewayTunnel.IpsecEncryption

### Microsoft.PowerShell Cmdletization.GenerateTypes.PS_GatewayTunnel.IpsecIntegrity

### Microsoft.PowerShell CmdletizationGeneratedTypes.PS_GatewayTunnel.Pfsgroup

### Microsoft.PowerShell Cmdletization.GenerateTypes.PS_GatewayTunnel.IkeEncryption

### Microsoft.PowerShell Cmdletization GeneratedTypes.PS_GatewayTunnel.IkeIntegrity

### Microsoft.PowerShell Cmdletization GeneratedTypes.PS_GatewayTunnel.Dhgroup

### System.UInt32

### Microsoft.PowerShell Cmdletization GeneratedTypes.PS_GatewayTunnel.ConnectReason

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#PS_GatewayTunnel

## 备注

## 相关链接
