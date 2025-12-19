---
external help file: GatewaytunnelConfig_v1.0.cdxml-help.xml
Module Name: Gatewaytunnel
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/gatewaytunnel/get-gatewaytunnel?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-GatewayTunnel
---

# Get-GatewayTunnel

## 摘要
{{ 请填写剧情简介 }}

## 语法

```
Get-GatewayTunnel [[-TunnelName] <String>] [[-RoutingDomainName] <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
{{ 填写描述内容 }}

## 示例

### 示例 1
```powershell
PS C:\> {{ Add example code here }}
```

{{ 在此处添加示例描述 }}

## 参数

### -AsJob
{{ 填写为工作描述 }}

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

### -CimSession
{{ 填写 CimSession 的描述 }}

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

### -ThrottleLimit
{{ 填写 ThrottleLimit 的描述 }}

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

### -TunnelName
{{ 填写隧道名称 | 描述 }}

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: Name

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.ManagementInfrastructure.CimInstance[]

### Microsoft.ManagementInfrastructure.CimInstance#PS_GatewayTunnel

## 备注

## 相关链接
